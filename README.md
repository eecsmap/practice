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
- now it should be available as https://eecsmap.github.io/practice/

## DNS setup
- add domain `eecs.pro` in github
- add custom domain `practice.eecs.pro` for this repository
- add CNAME `practice.eecs.pro` pointing to `eecsmap.github.io.`
- now we should be able to see it https://practice.eecs.pro

## verify the setup
- make change to `docs/index.md`
- verify the content at https://practice.eecs.pro
- create docs/data_structure/index.md
- update `mkdocs.yml` to make a navigation item
- verify the result

## best practice
- run `mkdocs serve` to do the local change
- keep updating [this](https://github.com/eecsmap/practice/blob/main/README.md) document
