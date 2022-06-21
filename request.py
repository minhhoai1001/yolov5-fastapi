import requests
import json

URL = 'http://172.17.0.1:8080/object-to-json'
files = {'file': open('zidane.jpg', 'rb')}

try:
    response = requests.post(URL, files=files)
    # print(response.content)

    response_dict = json.loads(response.text)
    for obj in response_dict:
        print(obj)
    # print(response_dict[0])

except:
    print("cannot conect to server")