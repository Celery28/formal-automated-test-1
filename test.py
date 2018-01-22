import re

totalCount = 'http://www.kgc.cn/course/17645?pid=20783'
totalCount = re.sub("\D", "", totalCount)
print(totalCount)

