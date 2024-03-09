env:
	poetry install

clean:
	rm -rf dist

package: clean
	mkdir dist
	poetry run python ci/scripts/package.py
	cd dist && zip -9 -r ../uk-vatis-profiles.zip . && cd ..
