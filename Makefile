test:
	python2 -m pytest .
	python3 -m pytest .

publish: clean test
	python3 setup/setup.py sdist
	python3 setup/setup.py bdist_wheel
	python3 -m twine upload dist/*

clean:
	-rm dist/ -r
	-rm *.egg-info/ -r
