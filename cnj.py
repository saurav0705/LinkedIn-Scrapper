import json
with open('raw_2000.txt', 'r') as outfile:
    data = json.load(outfile)

with open('raw_2000_validated.txt', 'w') as outfile:
    json.dump(data,outfile,indent=4)