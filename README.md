# practice

## setup
- create an empty github repository
- clone it locally
- `cd` into it
- run `mkdocs new .`
  - it will create `./mkdocs.yml` and `./docs/index.md`
- update `mkdocs.yml` to enable `material` theme
- update vscode `settings.json` for the yaml schema
- run `mkdocs serve` to preview
- run `mkdocs build` to build the site (folder)
- add github workflow
  - create `.github/workflows/ci.yml` with recommended content except removing the `master`
- push the changes
- set publishing source path for this github page as `gh-pages`
