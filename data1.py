import json 

empty_list = [] 


def write_json(data, filename='data.json'): 
    with open(filename, 'w') as f: 
        json.dump(data, f)
        

def append_to_list(list_name, filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        list_name.append(data)
    return list_name
    
        
print(f'Порожній список: {empty_list}')