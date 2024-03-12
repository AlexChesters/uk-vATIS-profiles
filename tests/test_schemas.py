import unittest
import os
import json

from parameterized import parameterized
from jsonschema import validate

# absolute path to the directory name this script lives in
SCRIPT_DIR = os.path.dirname(__file__)
dist_dir_path = os.path.join(SCRIPT_DIR, ".." , "dist")
schemas_dir = os.path.join(SCRIPT_DIR, "schemas")

positions = os.listdir(dist_dir_path)

class ProfilesSchemaTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand(positions)
    def test_schema_passes(self, position):
        with open(os.path.join(schemas_dir, position), "r", encoding="utf-8") as f:
            schema = json.load(f)

        with open(os.path.join(dist_dir_path, position), "r", encoding="utf-8") as f:
            profile = json.load(f)

        validate(instance=profile, schema=schema)
