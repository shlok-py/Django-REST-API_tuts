import requests
import json
URL = "http://127.0.0.1:8000/student_create/"
list = ["Santit", "Melina", "Rakshya"] 
roll = [26,28,3]
city = ["KTM", "Darchula", "Lalitpur"]
for i in range(6,10):
        
    data = {
        "id":i,
        "name": list[i-6],
        "Roll": roll[i-6],
        "city": city[i-6]
    }

    json_data = json.dumps(data)

    r = requests.post(URL, json_data)
    data = r.json()
    print(data)