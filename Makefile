.PHONY: default tools

default: tools

.venv/bin/uv:
	pip install uv

requirements.txt: requirements.in
	uv pip compile --generate-hashes --universal --quiet requirements.in -o requirements.txt

tool-requirements.txt: tool-requirements.in
	uv pip compile --generate-hashes --universal --quiet tool-requirements.in -o tool-requirements.txt

install: .venv/bin/uv tool-requirements.txt requirements.txt
	uv pip sync tool-requirements.txt requirements.txt