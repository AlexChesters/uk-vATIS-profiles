import os
import json

# find every position
# find every profile for every position
# combine to a single file per position, e.g.
# dist/
#   gmc.json
#   gmp.json

# absolute path to the directory name this script lives in
SCRIPT_DIR = os.path.dirname(__file__)
profiles_dir_path = os.path.join(SCRIPT_DIR, "..", "..", "profiles")
dist_dir_path = os.path.join(SCRIPT_DIR, ".." , "..", "dist")

positions = [
    (position.upper(), os.path.join(profiles_dir_path, position))
    for position in os.listdir(profiles_dir_path)
]

for position, position_path in positions:
    airfields = [
        os.path.join(position_path, airfield)
        for airfield in os.listdir(position_path)
    ]

    combined_profile = {
        "Name": position,
        "Composites": []
    }

    for airfield in airfields:
        with open(airfield, mode="r", encoding="utf-8") as f:
            airfield_data = json.load(f)
            combined_profile["Composites"].append(airfield_data)

    with open(f"{dist_dir_path}/{position.lower()}.json", mode="w", encoding="utf-8") as f:
        json.dump(combined_profile, f, indent=2)
