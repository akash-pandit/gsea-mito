# Mitochondria-specific GSEA

A gene-set enrichment analysis (GSEA) of various sets of mitochondria-related nuclear genes leading to support further study into the oxidative phosphorylation (OXPHOS in [MitoCarta 3.0](https://www.broadinstitute.org/mitocarta/mitocarta30-inventory-mammalian-mitochondrial-proteins-and-pathways)) gene set, provided in a documented and reproducible environment.

### Context

Genes are differentially expressed in cell populations, and a group of these genes that relate to some specific higher-order process/function are called a gene set, with that process/function being the 'pathway' that gene set is associated with. If the majority of the genes in a given pathway are highly enriched in either population, one can say the pathway itself is enriched in said population.

One of this lab's projects involves the discovery and study of a novel megakaryocyte progenitor (MkP, progenitor of platelet-producing MK) 'non-canonical' variant which, interestingly, shows increased function with age as opposed to their root parent ([Poscablo et al. 2021](https://doi.org/10.1016/j.stemcr.2021.04.016)). We hypothesize that mitochondrial function is a significant reason behind this shift, hence this analysis and the greater publication.

Read about GSEA [here](https://biostatsquid.com/gene-set-enrichment-analysis/).

- [Mitochondria-specific GSEA Analysis](#mitochondria-specific-gsea-analysis)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)

## Prerequisites

Basic BASH shell proficiency is assumed.

1. **Terminal Access**: Mac users use "Terminal". Windows users, please install/use[WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) or another BASH-based terminal emulator of your choice (e.g. Git Bash). 

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

**For VSCode Users**: VSCode sometimes struggles to recognize a UV environment. To force VSCode's internal jupyter server to recognize a uv python environment, run the following line:
```bash
uv run python -m ipykernel install --user --name internal_env_name --display-name "Env Name"
```
