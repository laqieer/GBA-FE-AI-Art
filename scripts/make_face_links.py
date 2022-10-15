#!/usr/bin/env python

import os
import json

links = []

with open('../../FE-Mod-Face-Search/refMap.json') as f:
    for v in json.load(f).values():
        links += [os.path.join('https://raw.githubusercontent.com/laqieer/FE-Mod-Face-Search/main/datasets/portraits/', os.path.basename(x)) for x in v]

print(links)
