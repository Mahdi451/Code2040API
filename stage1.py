import requests
import json

gitURL = "https://github.com/Mahdi451/Code2040API"
myData = {'token': 'dda85f37c000f36f63bbe0cc4226e83d', 'github': gitURL}

req = requests.post('http://challenge.code2040.org/api/register', myData)
