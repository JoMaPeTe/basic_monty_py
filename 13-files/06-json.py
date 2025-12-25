import json
user = {'name':'Jose','age':30,'active':True}

with open('datos.json','w') as file:
    json.dump(user, file, indent=4)

with open('datos.json','r') as file:
    data_read = json.load(file)
    print(data_read)