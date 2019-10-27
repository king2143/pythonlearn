# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:30:51 2019

@author: SAIC_G7066
"""
#match用法
import re
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('Hello\s.*\s\d{4}\s\w{5}',content)
print(result)
print(result.group())

#print(result.span())

#（）目标匹配
import re
result = re.match('^Hello\s(\d\d\d)\s(\d{4})\s(\w{10})',content)
print(result.group(0))
print(result.group(1))
print(result.group(2))

#通配符.*使用
import re
content = 'Hello 123 .?x4567 World_This is a Regex Demo'
result = re.match('^Hello\s(.*)\s\w{10}',content)
print(result.group(0))
print(result.group(1))

#贪婪匹配.*
import re
content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^He.*(\d+)\s\w{10}',content)
print(result.group(0))
print(result.group(1))

#非贪婪匹配.*？
import re
result = re.match('^He.*?(\d+)\s\w{10}',content)
print(result.group(0))
print(result.group(1))

#修饰符使用 re.S
import re
content1 = '''Hello 12
3 4567 World_This is a Regex Demo'''
result = re.match('^He.*?(\d+)\s\w{10}',content1,re.S)
print(result.group(0))
print(result.group(1))

#转义符使用 \
import re
content1 = '''H\ello 12
3 4567 World_This is a Regex Demo'''
result = re.match('^H\\el.*?(\d+)\s\w{10}',content1,re.S)
print(result.group(0))
print(result.group(1))

#search使用
import re
content1 = '''H.ello 12
3 4567 World_This is a Regex Demo'''
result = re.search('e.*?(\d+)\s\w{10}',content1,re.S)
print(result.group(0))
print(result.group(1))

#findall使用
import re
content1 = '''H.ello 12
3 4567 World_This is a Regex Demo
H.ello 12
3 7890 World_This is a Regex Demo'''
result = re.findall('e.*?(\d+)\s\w{10}',content1,re.S)
print(result)
print(result[0])
print(result[1])

#sub使用
import re
content1 = '''Hello 123 4567 World_This is a Regex Demo
Hello 123 7890 World_This is a Regex Demo'''
result = re.sub('\d','',content1,re.S)
print(result)
