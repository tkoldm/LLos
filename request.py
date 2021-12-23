import requests
from random import randint
from faker import Faker
import json

fake_data = Faker()

for i in range(5):
    data = {
        "first_name": fake_data.first_name(),
        "second_name": fake_data.last_name(),
        "last_name": fake_data.suffix(),
        "birthday": "06-10-2002",
        "course": randint(1, 5)
    }  
    req = requests.post("http://localhost:5000/student/", json=data)
    print(req.content)

list_stud = requests.get('http://localhost:5000/student/')
print(list_stud.content)

id_update = input("Input id for update: ")
data = {
        "first_name": fake_data.first_name(),
        "second_name": fake_data.last_name(),
        "last_name": fake_data.suffix(),
        "birthday": "06-10-2002",
        "course": randint(1, 5)
    }  
update = requests.put(f"http://localhost:5000/student/{id_update}", json=data)
print(update.content)

id_delete = input("Input id for delete: ")
data = {
        "first_name": fake_data.first_name(),
        "second_name": fake_data.last_name(),
        "last_name": fake_data.suffix(),
        "birthday": "06-10-2002",
        "course": randint(1, 5)
    }  
delete = requests.delete(f"http://localhost:5000/student/{id_delete}", json=data)
print(delete.content)