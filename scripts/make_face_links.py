#!/usr/bin/env python

import json

links = []

with open('../../FE-Mod-Face-Search/refMap.json') as f:
    for v in json.load(f).values():
        links += ['https://raw.githubusercontent.com/laqieer/FE-Mod-Face-Search/main/' + x[2:] for x in v]

print(links)
