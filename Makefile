.PHONY: venv

venv:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

clean:
	rm -rf venv/