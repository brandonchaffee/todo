import requests
import json
import re
with open('credentials.json') as f:
    credentials = json.load(f)

URL = 'https://api.github.com/users/'
username = credentials['username']
token = credentials['token']
spec = '/repos?access_token='

requestURL = URL + username + spec + token

r = requests.get(requestURL)

repoArray = []
for item in r.json():
    clone = item['clone_url'].encode("utf-8")
    repoName = re.search(username + '/(.*).git', clone).group(1)
    repoObj = { 'name': repoName, 'link': clone }
    repoArray.append(repoObj)

print(repoArray)
