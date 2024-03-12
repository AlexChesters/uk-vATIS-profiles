env:
	poetry install

clean:
	rm -rf dist

run: clean
	mkdir dist
	poetry run python -m uk_vatis_profiles.package

package: run
	cd dist && zip -9 -r ../uk-vatis-profiles.zip . && cd ..

test: run
	poetry run pytest -s .
	poetry run pylint uk_vatis_profiles
