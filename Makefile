.PHONY: help install-dev-deps test dist upload

help:
	@echo "Available targets"
	@echo "- test"
	@echo "- dist"
	@echo "- install-dev-deps"
	@echo "- upload (to PyPI, only for developers)"

install-dev-deps:
	python3 -m pip install --user --upgrade twine wheel tox pytest-cov

test:
	python3 -m tox

dist:
	python3 setup.py sdist bdist_wheel

upload: dist
	python3 -m twine upload dist/*