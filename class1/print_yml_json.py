#!/usr/bin/env python
import yaml
import json
from pprint import pprint as pp

with open("xfile.yml") as f:
    xlist_y = yaml.load(f)
pp(xlist_y)

with open("xfile.json") as f:
    xlist_j = json.load(f)
pp(xlist_j)

