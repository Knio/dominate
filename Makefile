test:
	python3 -m pytest . --ignore=tests/community

test-community:
	python3 -m pytest .

publish: clean test
	python3 -m build --no-isolation
	python3 -m twine upload dist/*

clean:
	-rm dist/ -r
	-rm build/ -r
	-rm *.egg-info/ -r
