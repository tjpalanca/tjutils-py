# Release notes

<!-- do not remove -->

## 0.10.1

* Update dependencies to latest versions

## 0.10.0

* Add a template workflow to plan and apply Terraform changes 
* Update default python version on github actions workflows to 3.11

## 0.9.1

* Update package dependencies.

## 0.9.0

* Fix redundant quarto declarations in tjdev_export, and ensure that `homepage`,
  `documentation` and `repository` are set in the `pyproject.toml` file.
* Update nbdev github actions poetry version to 1.2.2

## 0.8.4

### Bugfixes 

- `lib_path` only contains underscores to conform to how `poetry` installs the current package. 

## 0.8.3

### Minor Changes 

- Quarto preview options can be set within the `[tool.quarto]` section of `pyproject.toml`. 

### Bugfixes 

- Allow the theme to exist but not be part of the sidebar. 

## 0.8.2

### Bugfixes 

- Move the theme directory to `_theme` so quarto does not treat it like content.

## 0.8.1

### Bugfixes 

- Simplify default footer
- Make `tjdev_nbdev_theme` safer, don't overwrite unless explicitly specified. 

## 0.8.0

### New Features

- Add theming to the quarto website ([#2](https://github.com/tjpalanca/tjutils-py/issues/2))

### Changes 

- By default, `settings.ini` `recursive` option set to True 
- Reorganize github actions, limit pkg_testing workflow to pushes to master 

## 0.7.1

* Fix handling of branch name in `tjdev_export`.

## 0.7.0

* Update github actions to be more compatible with poetry-style nbdev.

## 0.6.6

* Change to using the local file versions instead of downloading from github
* Miscellaneous fixes

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
