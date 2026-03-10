# Mitochondria-specific GSEA Analysis

Conduct a GSEA of various non-oxphos mito gene sets to lead up to the interesting finds in the oxphos gene set.

### Context

Given preset 'sets' of mitochondrially-related genes, look for those sets between Young/Old HSCs that are statistically significant (GSEA).

Given: already tested OxPhos (oxidative phosphorylation) gene set and found some nice statistical significance, what do other gene sets look like? Proposed logic: 'we tested several mitochondrially-associated gene sets and found an interesting pattern among the oxidative phosphorylation set gene set'. The several sets would create Fig. 1A (Akash, this repo) which would lead into oxphos as Fig. 1B (Paloma)

Read about GSEA [here](https://biostatsquid.com/gene-set-enrichment-analysis/).

- [Mitochondria-specific GSEA Analysis](#mitochondria-specific-gsea-analysis)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)

## Prerequisites

Basic BASH shell proficiency is assumed. Mac users, this is built-in to your terminal. Windows users, please 

1. **Terminal Access**: Mac users use "Terminal". Windows users, please [install WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) or another BASH-based terminal emulator of your choice (e.g. Git Bash). 

2. **Git**: used for version control, [install here](https://git-scm.com/install/).

3. **uv**: Our Python package manager. Ensures that code runs the same way, no matter the machine. [Install it here](https://docs.astral.sh/uv/getting-started/installation/).

## Setup

To clone (download) this repository's contents, navigate to your parent directory of choice and run:
```bash
git clone https://github.com/akash-pandit/gsea-mito
cd gsea-mito
```

To download all python dependencies and configure your environment, run:
```bash
uv sync
uv pip install -e .
```

**For Jupyter users:** Launch jupyter with `uv` to ensure it uses the correct environment and navigate to one of the given URLs:
```bash
uv run jupyter lab
```

<!-- **For VSCode Users**: VSCode sometimes struggles to recognize a UV environment. To force VSCode's internal jupyter server to recognize a uv python environment, run the following line:
```bash
uv run python -m ipykernel install --user --name internal_env_name --display-name "Env Name"
``` -->
