import logging
import os
from typing import List, Union

from galaxy.util import listify
from galaxy.util.watcher import get_watcher
from tpv.core.loader import TPVConfigLoader
from tpv.core.mapper import EntityToDestinationMapper

log = logging.getLogger(__name__)


ACTIVE_DESTINATION_MAPPERS = {}
CONFIG_WATCHERS = {}


def load_destination_mapper(tpv_config_files: Union[List[str], str], reload=False):
    tpv_config_files = listify(tpv_config_files)
    log.info(f"{'re' if reload else ''}loading tpv rules from: {tpv_config_files}")
    loader = None
    for tpv_config_file in tpv_config_files:
        current_loader = TPVConfigLoader.from_url_or_path(tpv_config_file)
        if loader:
            loader.merge_loader(current_loader)
        else:
            loader = current_loader
    return EntityToDestinationMapper(loader)


def setup_destination_mapper(app, tpv_config_files: Union[List[str], str]):
    mapper = load_destination_mapper(tpv_config_files)

    def reload_destination_mapper(path=None):
        # reload all config files when one file changes to preserve order of loading the files
        global ACTIVE_DESTINATION_MAPPERS
        for tpv_config_files_str in ACTIVE_DESTINATION_MAPPERS:
            tpv_config_files = tpv_config_files_str.split(",")
            if path in tpv_config_files:
                ACTIVE_DESTINATION_MAPPERS[tpv_config_files_str] = load_destination_mapper(tpv_config_files, reload=True)

    for tpv_config_file in tpv_config_files:
        if os.path.isfile(tpv_config_file) and tpv_config_file not in CONFIG_WATCHERS:
            log.info(f"Watching for changes in file: {tpv_config_file}")
            CONFIG_WATCHERS[tpv_config_file] = (
                    CONFIG_WATCHERS.get(tpv_config_file) or
                    get_watcher(app.config, 'watch_job_rules', monitor_what_str='job rules'))
            CONFIG_WATCHERS[tpv_config_file].watch_file(tpv_config_file, callback=reload_destination_mapper)
            CONFIG_WATCHERS[tpv_config_file].start()
    return mapper


def map_tool_to_destination(
    app,
    job,
    tool,
    user,
    tpv_config_files: Union[List[str], str],
    job_wrapper=None,
    resource_params=None,
    workflow_invocation_uuid=None,
):
    global ACTIVE_DESTINATION_MAPPERS
    if not ','.join(tpv_config_files) in ACTIVE_DESTINATION_MAPPERS:
        ACTIVE_DESTINATION_MAPPERS[','.join(tpv_config_files)] = setup_destination_mapper(app, tpv_config_files)

    destination_mapper = ACTIVE_DESTINATION_MAPPERS[','.join(tpv_config_files)]
    return destination_mapper.map_to_destination(app, tool, user, job, job_wrapper, resource_params,
                                                        workflow_invocation_uuid)
