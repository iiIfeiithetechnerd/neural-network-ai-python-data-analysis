# this file is supposed to run on linux machines that are for users!
# In this specific case, this makefile is for my raspberry pi zero w.

VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

install: $(VENV)/bin/activate

$(VENV)/bin/activate: requirements.txt
	@echo "A new virtual environment is being created."
	python3 -m venv $(VENV)
	@echo "Pip is being upgraded."
	$(PIP) install --upgrade pip
	@echo "The libraries from requirements.txt are being installed."
	$(PIP) install -r requirements.txt
	touch $(VENV)/bin/activate

clean:
	rm -rf $(VENV)
	@echo "This environment has been removed."

.PHONY: install clean
