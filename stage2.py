import requests
import json

# In the future I should hide this key inside a file for security reasons
myToken = "dda85f37c000f36f63bbe0cc4226e83d"
gitURL = "https://github.com/Mahdi451/Code2040API"

myData = {'token': myToken, 'github': gitURL}
req = requests.post('http://challenge.code2040.org/api/reverse', myData)

# Grabbed the string and reversed it and passed it back to a variable
myString = req.text
print myString
reversedString = myString[::-1]
print reversedString

# Using the reversed string as my key
newData = {'token': myToken, 'string': reversedString}
req = requests.post('http://challenge.code2040.org/api/reverse/validate', newData)
print req
