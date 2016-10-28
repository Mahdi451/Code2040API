from datetime import timedelta
import requests
import dateutil.parser
import json
import iso8601

# In the future I should hide this key inside a file for security reasons
myToken = "dda85f37c000f36f63bbe0cc4226e83d"
gitURL = "https://github.com/Mahdi451/Code2040API"

myData = {'token': myToken, 'github': gitURL}
req = requests.post('http://challenge.code2040.org/api/dating', myData)
print req

# Loading corresponding data into their respective variable names
date = json.loads(req.text)['datestamp']
print date
interval = json.loads(req.text)['interval']
print interval

# They only told me about string-fu not time/date-fu, but seriously this was a challenge!
dateToString = dateutil.parser.parse(date)
print dateToString

#datestamp = dateToString + interval
newInterval = timedelta(seconds = interval)
print newInterval

# ......Not Working
#dateToString = dateToString.replace("+00:00", "Z")
#print dateToString

datestamp = (dateToString + newInterval).isoformat()
print datestamp

# Yeah! Almost there.
datestamp = datestamp.replace('+00:00', 'Z')
print datestamp

newData = {'token': myToken, 'datestamp': datestamp}
print newData

req = requests.post('http://challenge.code2040.org/api/dating/validate', json = newData)

print req
print req.text
