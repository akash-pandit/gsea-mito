# Figures

See generated GSEA (and maybe volcano) plots generated here, organized by directory named from `data/` file of origin. GO terms used come from the EnrichR `MSigDB_Hallmark_2020` database for mice.

- `preselected-terms.pdf`: a multi-GSEA figure showing enrichment for hardcoded pathways we are interested in.
- `top-10-terms-NES.pdf`: a multi-GSEA figure showing enrichment for the top 10 enriched pathways, as measured by magnitude (absolute value) of normalized enrichment score.

All figures are reproducible by cloning the repository and re-running `notebooks/gsea-mito-full-deg-list.ipynb` with the included input data present in `data/`. Customize values in the config cell for tweaked responses (e.g. top 15 or top 5 instead of top 20 most enriched genes, top N via adjusted p-value instead of NES, etc.).