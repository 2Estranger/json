import json

employee_json='{"name":"Prena","age":20,"state":"sikkim"}'

employee_dict=json.loads(employee_json)
print(employee_dict)

print(employee_dict['name'])


