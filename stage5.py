from datetime import timedelta
import requests
import dateutil.parser
import json

# In the future I should hide this key inside a file for security reasons
myToken = "dda85f37c000f36f63bbe0cc4226e83d"
gitURL = "https://github.com/Mahdi451/Code2040API"

myData = {'token': myToken, 'github': gitURL}
req = requests.post('http://challenge.code2040.org/api/dating', myData)
print req

date = json.loads(req.text)['datestamp']
print date
interval = json.loads(req.text)['interval']
print interval

dateToString = dateutil.parser.parse(date)
print dateToString

#datestamp = dateToString + interval
newInterval = timedelta(seconds = interval)
print newInterval

datestamp = dateToString + newInterval
print datestamp
#newData = {'token': myToken, 'datestamp': date}
#print newData

print req

# # Loading corresponding data into their respective variable names
# prefix = json.loads(req.text)['prefix']
# print prefix
# strings = json.loads(req.text)['array']
# #print strings
#
# # Some magical string-fu is happening in this line :D
# newToken = [arrays for arrays in strings if not arrays.startswith(prefix)]
# #print arrays
# print newToken
#
# newData = {'token': myToken, 'array': newToken}
# print newData
#
# req = requests.post('http://challenge.code2040.org/api/prefix/validate', json = newData)
# print req
