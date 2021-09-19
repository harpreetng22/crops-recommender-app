import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'N':90, 'P':42, 'K':42, 'temperature':20.879744,'humidity':82.002744, ph':6.502985, 'rainfall':202.935536, })

print(r.json())