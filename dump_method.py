import json

a={"name":"prena","age":20,"state":"sikkim"}
f=open("dump_method.json","w")
b=json.dump(a,f,indent=6)
f.close()