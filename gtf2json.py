 #!/usr/bin/python
    
import re
import fileinput
import sys
import json

Genes=sys.argv[1]
Find_G=[]
for lines in fileinput.input(Genes):
    matchGene=re.match(r'(^\w)+.*\sgene\s+(\w+)\s+(\w+)\s\W\s\W\s\W\s+\w+\s\W\w+\W\W\s\w+\s\W([\w\.\w-]+)',lines,re.M)
    if matchGene:
        #print("matchGene.group():",matchGene.group())
        C=matchGene.group(1)
        SP=matchGene.group(2)
        EP=matchGene.group(3)
        GN=matchGene.group(4)
        Find_GN={"geneName":GN}
        Find_C={"chr":C}
        Find_SP={"startPos":SP}
        Find_EP={"endPos":EP}
        Find_G.append(Find_GN)
        Find_GN.update(Find_C)
        Find_GN.update(Find_SP)
        Find_GN.update(Find_EP)
        
with open("dzy.json","w") as f:
    json.dump(Find_G,f)
