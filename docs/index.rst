.. image:: images/vortex-logo-wide.png

.. centered::

   **Dynamic rules for mapping Galaxy resources to destinations**

TotalPerspectiveVortex (Vortex) provides an installable set of dynamic rules for the
`Galaxy application`_ that can route resources (Tools, Users, Roles) to appropriate
destinations based on a configurable yaml file. The aim of Vortex is to build on and
unify previous efforts, such as `Dynamic Tool Destinations`_, the `Job Router`_ and
`Sorting Hat`_, into a configurable set of rules that that can be extended arbitrarily
with custom Python logic.

How it works
------------
Vortex provides a dynamic rule that can be plugged into Galaxy via ``job_conf.xml``.
The dynamic rule will also have an associated configuration file, that maps resources
(tools, users, roles) to specific destination through a flexible tagging system.
Destinations can have arbitrary tags defined, and each resource can express a preference
or aversion to specific tags. Based on this tagging, jobs are routed to the most appropriate
destination. In addition, admins can also plugin arbitrary python based rules for making
more complex decisions, as well as custom ranking functions for choosing between matching
destinations. For example, a ranking function could query influx metrics to determine
the least loaded destination, and route jobs there, providing a basic form of
"metascheduling" functionality.

Getting Started
---------------

1. `pip install total-perspective-vortex` into Galaxy's python virtual environment
2. Configure Galaxy to use Vortex's dynamic destination rule
3. Create the vortex job mapping yaml file, indicating job routing preferences
4. Submit jobs as usual


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   topics/configure_galaxy.rst
   topics/configure_vortex_rules.rst

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Galaxy application: https://galaxyproject.org/
.. _Dynamic Tool Destinations: https://training.galaxyproject.org/training-material/topics/admin/tutorials/job-destinations/tutorial.html
.. _Job Router: https://github.com/galaxyproject/usegalaxy-playbook/blob/c674b4795d63485392acd55bf6b4c7fb31754f5d/env/common/files/galaxy/dynamic_rules/job_router.py
.. _Sorting Hat: https://github.com/usegalaxy-eu/sorting-hat