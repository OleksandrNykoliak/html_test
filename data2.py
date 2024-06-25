from os import write
from data1 import empty_list, write_json, append_to_list


write_json('1', 'data.json')

append_to_list(empty_list, 'data.json')

print(f'Порожній список: {empty_list}')
 

