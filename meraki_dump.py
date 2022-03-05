import json

a={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    }
}
ex=open('meraki_dump.json','w')
json.dump(a,ex,indent=6)
ex.close()