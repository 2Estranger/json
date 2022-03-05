import json 

f=open("meraki_dump.json",)

f1=json.load(f)

for i in f1['emp1']:
    print(i)
    
f.close()
