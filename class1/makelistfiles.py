#!/usr/bin/env python

import yaml
import json

xlist = range(7)
xlist.append('First Thing')
xlist.append('Second Thing')
xlist.append({})
xlist[-1]["ip_address"] = "172.16.22.22"
xlist[-1]["attribs"] = range(8)

with open("xfile.yml" , "w") as f:
    yaml.dump(xlist, f)

with open("xfile.json" , "w") as f:
    json.dump(xlist, f)
 
