import requests
import time

url = 'http://api.open-notify.org/iss-now.json'

while True:
    response = requests.get(url) 
    print(response) 
    data = response.json()
    print(data['iss_position'])
    time.sleep(1) 