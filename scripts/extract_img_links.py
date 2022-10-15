#!/usr/bin/env python

import re
import sys

links = []

with open(sys.argv[1]) as f:
    for l in f.readlines():
        links += re.findall(r'https://.*?png', l)

print(links)
