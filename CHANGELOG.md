# Release notes

<!-- do not remove -->

## 0.6.0

* Feature: Add ability to import gitignore for nbdev projects

## 0.5.1

* Fix wrong command for `tjdev_release`

## 0.5.0

* Feature: `tjdev_release` release to both git and pypi 
* Feature: `tjdev_export` now formats the notebooks with `{black}`

## 0.4.4

* Bugfix, `status` and other variables not set

## 0.4.3

* Custom sidebar and cosmetic fixes

## 0.4.2

* Back to 3.9 again, not working

## 0.4.1

* Require back to Python 3.11 but add .python-version file to `github_actions()` in order to satisfy the function.

## 0.4.0

* Require only Python 3.10 to enable GitHub Actions. As a result, switch from `tomllib` to `tomli`.
R
## 0.3.0

* Add Github Actions 
* Feature: `tjdev_nbdev_gha` adds test and docs deployment github actions

## 0.2.1

* Fix unexported command for poetry 
* Updates to documentation

## 0.2.0

* Change: Renamed `tj_nbdev_*` scripts to `tjdev_*`
* Feature: `tjdev_version` updates both poetry and nbdev versions 

## 0.1.3

* Bugfix: `export()` feature didn't work outside of the notebook
* Feature: `tj_nbdev_export` CLI script

## 0.1.2

* Feature: `export()` now covers all required `settings.ini` options and uses `pyproject.toml` as the canonical source to overwrite anything.

## 0.1.1

* Feature: `export()` exports basic data from Poetry's pyproject.toml and nbdev's settings.ini
