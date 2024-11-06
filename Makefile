.PHONY: test

install: .venv
	. .venv/bin/activate && python -m pip install -r requirements.txt

.venv:
	python -m venv .venv

test:
	. .venv/bin/activate && python -m pytest