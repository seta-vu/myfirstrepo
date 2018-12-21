import json
from pprint import pprint
with open('config.json') as f:
    engines = json.load(f)
    pprint(engines)

for engine in engines["engines"]:
    print(engine["id"])
