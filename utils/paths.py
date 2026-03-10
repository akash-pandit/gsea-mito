import pyrootutils

ROOT = pyrootutils.setup_root(
    search_from=__file__,
    indicator="pyproject.toml",
    project_root_env_var=True,
    dotenv=True,
    pythonpath=True,
    cwd=True,
)

DATA = ROOT / "data"
FIGURES = ROOT / "figures"
UTILS = ROOT / "utils"