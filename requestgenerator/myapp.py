import requests
url = "http://127.0.0.1:8000/student/2"
r = requests.get(url)
data = r.json()
print(data)