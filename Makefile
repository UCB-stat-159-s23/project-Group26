# run everything in the same shell
.ONESHELL:
SHELL:= /bin/bash

# Name of the conda environment
CONDA_ENV_NAME = projenv

# install the environment
.PHONY: env
env:
    source /srv/conda/etc/profile.d/conda.sh # configure shell to use 'conda activate'. 
    conda env create -f environment.yml -p ~/envs/$(CONDA_ENV_NAME)
    conda activate $(CONDA_ENV_NAME)
    python -m ipykernel install --user --name $(CONDA_ENV_NAME) --display-name "$(CONDA_ENV_NAME)"

# run all the notebooks
.PHONY: all
all: 
    jupyter execute sfevictions.ipynb --kernel_name=$(CONDA_ENV_NAME)   
    jupyter execute main.ipynb --kernel_name=$(CONDA_ENV_NAME)

# remove the environment
.PHONY: remove-env
remove-env:
    source /srv/conda/etc/profile.d/conda.sh # configure shell to use 'conda activate'. 
    conda deactivate 
    mamba env remove -n $(CONDA_ENV_NAME)

# update the environment
.PHONY: update-env
update-env:
    mamba env update --file environment.yml --prune
    conda activate $(CONDA_ENV_NAME)
    python -m ipykernel install --user --name $(CONDA_ENV_NAME) --display-name "$(CONDA_ENV_NAME)"
    


# clean up the generated figures, tables and _build folders.
.PHONY: clean
clean:
    rm -rf plots/*
    cd plots && touch .gitkeep   