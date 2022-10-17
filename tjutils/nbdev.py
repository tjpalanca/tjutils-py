# AUTOGENERATED! DO NOT EDIT! File to edit: ../notebooks/01-nbdev.ipynb.

# %% auto 0
__all__ = ['BumpRule', 'generate', 'export', 'version', 'github_actions', 'release', 'gitignore', 'theme']

# %% ../notebooks/01-nbdev.ipynb 1
import tomli
import tomlkit
import subprocess  # nosec
import yaml
from fastcore.xtras import repo_details
from nbdev import nbdev_export
from nbdev.config import read_config_file, get_config
from configparser import ConfigParser
from pathlib import Path
from git import Repo
from urllib.parse import urlparse
from fastcore.script import call_parse
from enum import Enum
from .utils import copy_template, copy_directory, copy_yaml
from nbdev.release import release_gh

# %% ../notebooks/01-nbdev.ipynb 2
def _poetry_command(*args):
    subprocess.run(["poetry", *args])  # nosec


def _black_command(*args):
    subprocess.run(["black", *args])  # nosec


class BumpRule(Enum):
    prerelease = 0
    major = 1
    premajor = 2
    minor = 3
    preminor = 4
    patch = 5
    prepatch = 6

# %% ../notebooks/01-nbdev.ipynb 3
def _get_classifier_value(classifiers, name):
    if classifiers is None:
        return None
    classifier = [c for c in classifiers if c.startswith(f"{name} :: ")]
    if len(classifier) == 1:
        return classifier[0].split(" :: ")[1]
    else:
        return None


def generate():
    """
    Infer information from poetry's `pyproject.toml` and the git repository information
    and generate:

    * a compliant `settings.ini` file for nbdev, and
    * a compliant `_quarto.yml` file for the quarto-based documentation, and
    * a filled-in `pyproject.toml` for poetry.

    Most poetry configs are mapped to the fields that make sense, but for configs that
    are not present in pyproject.toml, they can be supplied via a `[tool.nbdev]` section
    in pyproject.toml.
    """

    # Read pyproject.toml
    pyproject_file = Path("pyproject.toml")
    with pyproject_file.open("rb") as f:
        pyproject = tomli.load(f)
    poetry = pyproject["tool"]["poetry"]
    nbdev = pyproject["tool"].get("nbdev") or {}
    quarto = pyproject["tool"].get("quarto") or {}

    # Read git repository
    repo = Repo(".")
    git_url = repo.remotes["origin"].url
    git_user, git_repo = repo_details(repo.remotes["origin"].url)

    # Gather as much config from data sources
    authors = ", ".join(aut.split("<")[0].strip() for aut in poetry["authors"])
    site_url = poetry.get("homepage", f"https://tjpalanca.com/{git_repo}")
    docs_url = poetry.get("documentation", site_url)
    doc_url = urlparse(docs_url)
    doc_host = f"{doc_url.scheme}://{doc_url.netloc}"
    doc_baseurl = doc_url.path
    classifiers = poetry.get("classifiers")
    if status := _get_classifier_value(classifiers, "Development Status"):
        status = status.split(" - ")[0]
    audience = _get_classifier_value(classifiers, "Intended Audience")
    language = _get_classifier_value(classifiers, "Natural Language")
    inferred = {
        "repo": git_repo,
        "branch": nbdev.get("branch", "master"),
        "user": git_user,
        "author": authors,
        "author_email": ", ".join(
            aut.split("<")[1].replace(">", "") for aut in poetry["authors"]
        ),
        "description": poetry["description"],
        "path": nbdev.get("path", "."),
        "cfg_name": nbdev.get("cfg_name", "settings.ini"),
        "lib_name": poetry["name"],
        "git_url": git_url,
        "custom_sidebar": nbdev.get("custom_sidebar", "False"),
        "nbs_path": nbdev.get("nbs_path", "notebooks"),
        "lib_path": poetry["name"].replace("-", "_"),
        "doc_path": nbdev.get("doc_path", "_docs"),
        "tst_flags": nbdev.get("tst_flags", "notest"),
        "version": poetry["version"],
        "doc_host": nbdev.get("doc_host", doc_host),
        "doc_baseurl": nbdev.get("doc_baseurl", doc_baseurl),
        "keywords": poetry.get("keywords", "tjpalanca nbdev"),
        "license": poetry["license"],
        "copyright": f"2022 onwards, {authors}",
        "status": nbdev.get("status") or status or ("3"),
        "audience": nbdev.get("audience") or audience or ("Developers"),
        "min_python": poetry["dependencies"]["python"].replace("^", ""),
        "language": nbdev.get("language") or language or ("English"),
        "recursive": nbdev.get("recursive", "True"),
        "black_formatting": nbdev.get("black_formatting", "True"),
        "readme_nb": nbdev.get("readme_nb", "index.ipynb"),
        "title": poetry["name"],
        "allowed_metadata_keys": nbdev.get("allowed_metadata_keys"),
        "allowed_cell_metadata_keys": nbdev.get("allowed_cell_metadata_keys"),
        "jupyter_hooks": nbdev.get("jupyter_hooks", "True"),
        "clean_ids": nbdev.get("clean_ids", "True"),
        "clear_all": nbdev.get("clear_all", "False"),
        "put_version_in_init": nbdev.get("put_version_in_init", "True"),
    }

    # Unify with existing settings.ini
    settings_file = Path("settings.ini")
    if settings_file.is_file():
        config = dict(read_config_file(settings_file)) | inferred
        settings_file.unlink()
    else:
        config = inferred

    # Write _quarto.yml
    quarto_file = Path(config["nbs_path"]) / "_quarto.yml"
    if quarto_file.is_file():
        with quarto_file.open("r") as f:
            quarto_data = yaml.safe_load(f)
        quarto_data["project"]["preview"] = {
            "host": quarto.get("host", "0.0.0.0"),
            "port": quarto.get("port", 8888),
            "browser": quarto.get("browser", False),
        }
        with quarto_file.open("w") as f:
            yaml.safe_dump(quarto_data, f)

    # Write pyproject.toml
    with pyproject_file.open("r") as f:
        pyproject_data = tomlkit.load(f)
    pyproject_data["tool"]["poetry"]["homepage"] = site_url
    pyproject_data["tool"]["poetry"]["documentation"] = docs_url
    pyproject_data["tool"]["poetry"]["repository"] = git_url
    with pyproject_file.open("w") as f:
        tomlkit.dump(pyproject_data, f)

    # Write settings.ini
    config = {k: v for k, v in config.items() if v is not None}
    path = config.pop("path")
    name = config.pop("cfg_name")
    parser = ConfigParser()
    parser["DEFAULT"] = config
    with settings_file.open("w") as f:
        parser.write(f)

    # Format ipynb with black
    _black_command(config["nbs_path"])

# %% ../notebooks/01-nbdev.ipynb 4
def export():
    "Similar to `nbdev_export`"
    generate()
    nbdev_export.__wrapped__()

# %% ../notebooks/01-nbdev.ipynb 5
@call_parse
def version(rule: str):  # PEP-440 compliant bump rule
    _poetry_command("version", BumpRule[rule].name)
    export()

# %% ../notebooks/01-nbdev.ipynb 6
def github_actions():
    "Add GitHub Actions Workflows"
    copy_template(
        "nbdev/github_actions/doc_deploy.yml", ".github/workflows/doc_deploy.yml"
    )
    copy_template(
        "nbdev/github_actions/pkg_testing.yml", ".github/workflows/pkg_testing.yml"
    )

# %% ../notebooks/01-nbdev.ipynb 7
def release():
    "Creates a release on github and poetry"
    release_gh()
    _poetry_command("build")
    _poetry_command("publish")

# %% ../notebooks/01-nbdev.ipynb 8
def gitignore():
    "Appends to the gitignore for nbdev specific ignores."
    copy_template("nbdev/gitignore", ".gitignore", append=True)

# %% ../notebooks/01-nbdev.ipynb 9
@call_parse
def theme(overwrite=False):
    "Adds the TJ Palanca theme to quarto"
    config = get_config()
    # Copy assets
    theme_dir = config["nbs_path"] / "theme"
    if not theme_dir.is_dir() or overwrite:
        copy_directory("nbdev/theme", str(theme_dir))
    # Merge in _quarto.yml
    quarto_file = config["nbs_path"] / "_quarto.yml"
    if not quarto_file.is_file() or overwrite:
        copy_yaml("nbdev/_quarto.yml", str(quarto_file))
