# Release notes

<!-- do not remove -->

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
