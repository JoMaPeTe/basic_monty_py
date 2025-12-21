nested_dict = {
    'Persona1': {'Nombre':'Pepe','edad':"29", 'ciudad':'Vigo'},
    'Persona2': {'Nombre':'Alex','edad':"19", 'ciudad':'Stocolm'},
    'Persona3': {'Nombre':'Alfred','edad':"23", 'ciudad':'Toronto'},
}
print(nested_dict)

for key,value in nested_dict.items():
    # print(key,value)
    print(f"{key}:")
    for sub_key, sub_value in value.items():
        print(f" {sub_key}: {sub_value}")