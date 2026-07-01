# TPV Overview Site

This folder contains the static overview website for Total Perspective Vortex.
The site explains what TPV is, how it is used in the Galaxy ecosystem, and links
readers to the canonical docs, source code, shared database, tutorial, and
paper.

## Folder Layout

- `src/pages/index.astro` is the homepage content and structure.
- `src/styles/global.css` contains the Galaxy-inspired visual styling.
- `public/` contains static assets copied into the built site, including the
  TPV logo, dispatch diagram, and `CNAME`.
- `tests/site-content.test.mjs` checks that required content, links, assets,
  and the custom domain are present.
- `astro.config.mjs`, `package.json`, and `tsconfig.json` define the Astro
  static-site build.

## Run Locally

Install dependencies from this folder:

```bash
cd site
npm install
```

Run the local development server:

```bash
npm run dev
```

Astro will print the local URL, usually `http://localhost:4321/`.

Run the content test:

```bash
npm test
```

Build the static site:

```bash
npm run build
```

Preview the production build:

```bash
npm run build
npx astro preview
```

The generated static files are written to `site/dist/`.

## GitHub Pages Setup

The repository includes `.github/workflows/pages.yaml`, which publishes this
folder to GitHub Pages.

To enable it:

1. In the GitHub repository settings, open **Pages**.
2. Set **Build and deployment** source to **GitHub Actions**.
3. Push changes to `main`, or manually run the `Publish TPV overview site`
   workflow.
4. The workflow installs dependencies with `npm ci`, runs `npm test`, builds
   with `npm run build`, uploads `site/dist`, and deploys it to Pages.

## Custom Domain

The site is configured for:

```text
tpv.galaxyproject.org
```

`public/CNAME` contains that domain, so the built Pages artifact includes the
required `CNAME` file.

After GitHub Pages is enabled, configure DNS for `tpv.galaxyproject.org` as a
CNAME pointing at the GitHub Pages hostname for this repository, typically:

```text
galaxyproject.github.io
```

Then add `tpv.galaxyproject.org` as the custom domain in the repository's
GitHub Pages settings and enable HTTPS once GitHub finishes provisioning the
certificate.
