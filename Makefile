default:
	@echo "Please choose one of the following target: dep, clean, run"
	@exit 2

dep: clean
	virtualenv --python=python3.8 ./venv
	./venv/bin/python setup.py install
	./venv/bin/pip freeze > requirements.txt

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf ./venv
	rm -rf *.egg-info