test:
	-python2 -m pytest .
	python3 -m pytest .

publish_old: clean test
	python3 setup/setup.py sdist
	python3 setup/setup.py bdist_wheel
	python3 -m twine upload dist/*

publish: clean test
	python3 -m build --no-isolation
	python3 -m twine upload dist/*

clean:
	-rm dist/ -r
	-rm build/ -r
	-rm *.egg-info/ -r
