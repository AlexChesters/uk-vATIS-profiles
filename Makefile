env:
	poetry install

clean:
	rm -rf dist

package: clean
	mkdir dist
	poetry run python ci/scripts/package.py
