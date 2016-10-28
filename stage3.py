import requests
import json

# In the future I should hide this key inside a file for security reasons
myToken = "dda85f37c000f36f63bbe0cc4226e83d"
gitURL = "https://github.com/Mahdi451/Code2040API"

myData = {'token': myToken, 'github': gitURL}
req = requests.post('http://challenge.code2040.org/api/haystack', myData)

# Loading corresponding data into their variable names
needle = json.loads(req.text)['needle']
print needle
haystack = json.loads(req.text)['haystack']
print haystack

# Searching for needle in haystack
index = -1
if needle in haystack:
    index = haystack.index(needle)
print index

newToken = {'token': myToken, 'needle': index}
print newToken
req = requests.post('http://challenge.code2040.org/api/haystack/validate', newToken)

print req
