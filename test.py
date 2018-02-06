import re

totalCount = 'http://www.kgc.cn/course/17645?pid=20783'
nuberr = "笔记 2"
totalCount = re.sub("\D", "", nuberr)
print(totalCount)

a = []
print(len(a))

m = "课程：大数据开发工程师2.0"
print(m.split("："))


a = 'Beautiful, is; better*than\nugly'
# 四个分隔符为：,  ;  *  \n
x = re.split('：',m)
print(x)

