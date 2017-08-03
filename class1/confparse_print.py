from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

print "#" * 10
print "All crypto maps:"

maps = cisco_cfg.find_objects("^crypto map")

for map_ in maps:
    print map_.text
    for child in map_.children:
        print child.text

print "\n\n"
print "#" * 10
print "Crypto maps using pfs group2:"

g2maps = cisco_cfg.find_objects_w_child(parentspec = "^crypto map", childspec = "set pfs group2")

for g2map in g2maps:
   print g2map.text

print "\n\n"
print "#" * 10
print "Crypto maps not using AES transform set:"

nonAESmaps = cisco_cfg.find_objects_wo_child(parentspec = "^crypto map", childspec = "AES")

for nonAESmap in nonAESmaps:
    print nonAESmap.text
    for nchild in nonAESmap.children:
        if "transform-set" in nchild.text:
            print nchild.text



