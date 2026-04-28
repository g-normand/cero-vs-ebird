### Configure paths. ###
PROJECT_PATH := $(CURDIR)
ENV_PATH := $(CURDIR)/filters_env
PYTHON := $(ENV_PATH)/bin/python3.11
TAG_NAME := DEPLOY
TAG_DATE := $(TAG_NAME)_$(shell date -u "+%Y_%m_%d_%H_%M_%S")

### Shell configure. ###
# For shell to bash to be able to use source.
SHELL = /bin/bash

# Shortcut to set env command before each python cmd.
VENV = source $(ENV_PATH)/bin/activate

# Config is based on two environment files, initalized here.
virtualenv: $(ENV_PATH)/bin/activate

$(ENV_PATH)/bin/activate:
	virtualenv -p /usr/bin/python3.11 $(ENV_PATH)

### Manage project installation. ###
# Install python requirements.
pip: virtualenv
	$(VENV) && cd $(CURDIR) && pip3 install -r $(CURDIR)/requirements.txt;

clean:
	find . -name '*.pyc' -delete
diff_cero_and_ebird:
	$(VENV) && python3 diff_cero_and_ebird.py
	
	

deploy:
	npm run build
	scp -r dist/* guiguide@ssh-guiguide.alwaysdata.net:/home/guiguide/www/cero_vs_ebird/
	git tag $(TAG_DATE); git push origin $(TAG_DATE) --no-verify

processSpecies:
	npm run processSpecies

dev:
	npm run dev
