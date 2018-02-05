import re

totalCount = 'http://www.kgc.cn/course/17645?pid=20783'
nuberr = "笔记 2"
totalCount = re.sub("\D", "", nuberr)
print(totalCount)

