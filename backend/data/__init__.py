import json
import pprint

pp = pprint.PrettyPrinter(indent=4)

with open('harrastukset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    pp.pprint(data)