# import requests
# url = "http://127.0.0.1:8000/student/2"
# r = requests.get(url)
# data = r.json()
# print(data)

import requests
import json

def get_request(url, id = None):
    data = {}
    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    r = requests.get(url, data = json_data)
    
    data = r.json()
    print(data)

def create_insert_data(url, id, name, roll, city):
    data = {
        'id': id,
        'name': name,
        'Roll': roll,
        'city': city
    }
    json_data = json.dumps(data)
    r = requests.post(url, json_data)
    data = r.json()
    print(data)

def update_data(url, id, name="", roll=None, city=""):
    data = {
        'id': id,
        'name': name,
        'Roll': roll,
        'city': city
    }
    json_data = json.dumps(data)
    r = requests.put(url, json_data)
    data = r.json()
    print(data)

def delete_data(url, id):
    data = {
        'id': id
    }
    json_data = json.dumps(data)
    r = requests.delete(url, data = json_data)
    data = r.json()
    print(data)
    
if __name__ == "__main__":
    url = "http://127.0.0.1:8000/studentapi/"
    get_request(url)
    create_insert_data(url,2, "Ansan", 1, "KTM")
    # update_data(url, 1, "R Shlok", 3, "BR")
    # delete_data(url,13)