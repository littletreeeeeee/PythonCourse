# encoding=UTF-8
import requests

base_url = 'https://pythoncourse-4e7b5.firebaseio.com/%s.json'
url4 = base_url % 'demo4'
url5 = base_url % 'demo5'

json4 = {'3': 'Newly HEY', '2': 1.23, '6': u'獅子 猴子'}
result4 = requests.patch(url4, json=json4)
print result4.status_code, result4.content

json5 = {'instructor': 'Mark', 'duration': 36}
result5 = requests.patch(url5, json=json5)
print result5.status_code, result5.content
