import requests
url = 'http://localhost:5000/api'
r = requests.get(url,json={'exp':"Forrest Gump",})
print(r.json()) 
