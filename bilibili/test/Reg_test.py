import re

a = 'https://www.bilibili.com/video/av2271112/'

num = re.sub('.+/av|/$','',a)
print(num)