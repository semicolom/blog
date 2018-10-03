PIP="venv/bin/pip"
TMP_PIP="temp_venv/bin/pip"
PYTHON="venv/bin/python"
ISORT="venv/bin/isort"
FLAKE8="venv/bin/flake8"
COVERAGE="venv/bin/coverage"

REQUIREMENTS:=requirements/requirements.txt
REQUIREMENTS_BASE:=requirements/base.txt
REQUIREMENTS_TEST:=requirements/test.txt

ARTIFACT:=blog.tar.gz
PIP_DOWNLOAD:=.pip_download

.PHONY: requirements

clean:
	@find . -name *.pyc -delete
	@rm -rf venv $(PIP_DOWNLOAD)
	@rm -f $(ARTIFACT)

requirements:
	virtualenv -p python3.6 temp_venv
	$(TMP_PIP) install -U "pip"
	$(TMP_PIP) install -r $(REQUIREMENTS_BASE)
	$(TMP_PIP) freeze | grep -v "pkg-resources" > requirements/requirements.txt
	@rm -rf temp_venv

virtualenv_base:
	test -d venv || virtualenv -p python3.6 venv
	$(PIP) install -U "pip"

virtualenv: virtualenv_base
	$(PIP) install -r $(REQUIREMENTS_TEST)

install: virtualenv_base
	$(PIP) install -I --no-index --find-links=$(PIP_DOWNLOAD) $(PIP_DOWNLOAD)/*

build: clean virtualenv_base
	@mkdir $(PIP_DOWNLOAD)
	$(PIP) download --dest $(PIP_DOWNLOAD) -r $(REQUIREMENTS)
	@tar -czf $(ARTIFACT) --exclude=venv --exclude=.git --exclude=$(ARTIFACT) * $(PIP_DOWNLOAD)

isort: virtualenv
	$(ISORT) -rc -y src/

test: virtualenv
	$(ISORT) -rc -c src/
	$(FLAKE8) src/
	$(COVERAGE) run --source='src/' src/manage.py test src/
	$(COVERAGE) report
