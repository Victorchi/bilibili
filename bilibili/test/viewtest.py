import requests
import re
import json
ItemView = {}
url ='https://api.bilibili.com/x/web-interface/archive/stat?callback=jQuery1720735417825650772_1506562164551&aid=2271112&jsonp=jsonp'
response = requests.get(url).text
response = re.sub('.*\d\(|\)$','',response)
json = json.loads(response)
ItemView['aid'] = json['data']['aid']
ItemView['view'] = json['data']['view']
ItemView['danmaku'] = json['data']['danmaku']
ItemView['favorite'] = json['data']['favorite']
ItemView['coin'] = json['data']['coin']
ItemView['share'] = json['data']['share']
print(ItemView)