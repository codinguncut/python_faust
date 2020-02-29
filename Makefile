all: install

pip-tools:
	pip install pip-tools

requirements.txt: requirements.in
	pip-compile requirements.in --upgrade

install: pip-tools requirements.txt requirements-dev.txt
	pip-sync requirements-dev.txt requirements.txt
	pip install -r requirements-dev.txt
	pip install -r requirements.txt
	CFLAGS="-Wno-narrowing" pip install cld2-cffi
	# python -m spacy download en_core_web_lg
	python -m spacy download en
	cp sample.env .env
	# alternatively, use pycld2
