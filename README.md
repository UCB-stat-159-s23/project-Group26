# Analyzing Evictions in the City of San Francisco

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s23/project-Group26/HEAD)

Link to our book: https://ucb-stat-159-s23.github.io/project-Group26/EvictionsMain.html

Authors: Yiran Li, Carrie Hu, Angelo Punzalan, Oona Risse Adams

## Introduction
In this notebook, we will take in the Eviction_Notices.csv file from https://catalog.data.gov/dataset/eviction-notices and analyze any possible patterns of evictions in San Francisco.

San Francisco is known as one of the more expensive cities to live in the United States, ranking number 20 in the 2022-2023 U.S. News Rankings. Within San Francisco, there are a myriad of different neighborhoods, each with their own unique aesthetic. However, the good sides always come with the bad. Seeing as how rent prices keep getting higher and more difficult to afford within the Bay Area, we decided to analyze some data and see if there were any particular reasons tenants got evicted other than inability to pay rent. 

Installation Instructions

To set up a new conda environment with the necessary dependencies, run make env. Activate the environment with conda activate projenv. Use the projenv kernel to run the Jupyter Notebook.

To utilize the custom functions designed specifically for this project, you'll need to install the tools package. Please restart the kernel after installation. This is because the running kernel does not continuously monitor changes in the installed packages.


## Repository Structure

- `data/` contains different datasets in csv and json formats
  - `Eviction_Notices.csv`
  - `Sanfrancisco.Neighborhoods.json`
  - `updated-file.json`
- `figs`, `plots` contains generated figures from running the notebook `main.ipynb`
- `tools` contains the package, which has all the tailor-made functions for this project
- `_config.yml` required for JupyterBook
- `conf.py` required for JupyterBook
- `_toc.yml` is the table of contents for JupyterBook
- `environment-jupyterbook.txt` packages for the book build in Github Actions
- `environment.yml` is the conda environment for this repo.
- `Makefile` make commands for easy execution
- `LICENSE` contains the license used by the repo
- `README.md` current document

## Makefile Commands

`make`
- `env` creates and configures the environment
- `remove-env` remove the environment
- `update-env` update the environment
- `html` build the JupyterBook normally
- `clean` clean up the generated figures and _build folders.
- `all` run all the notebooks



