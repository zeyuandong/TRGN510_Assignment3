import re
import fileinput
import sys
import json

Genes=sys.argv[1]
Find_G=[]
for line in fileinput.input(Genes):
    matchGene=re.match(r'(^\w)+.*\sgene\s+(\w+)\s+(\w+)\s\W\s\W\s\W\s+\w+\s\W\w+\W\W\s\w+\s\W(\w+)',line,re.M|re.I)
    if matchGene:
        #print("matchGene.group():",matchGene.group())
        C=matchGene.group(1)
        SP=matchGene.group(2)
        EP=matchGene.group(3)
        GN=matchGene.group(4)
        for line1 in GN:
            for line2 in SP:
                for line3 in EP:
                    for line4 in EP:
                        Find_GN={"geneName":GN}
                        Find_C={"chr":C}
                        Find_SP={"startPos":SP}
                        Find_EP={"endPos":EP}
                        Find_G.append(Find_GN)
                        Find_GN.update(Find_C)
                        Find_GN.update(Find_SP)
                        Find_GN.update(Find_EP)
                        FindGene=json.dumps(Find_G)
print(FindGene)
print(Find_G)
