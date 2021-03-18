

import re, textwrap

str = """Python is an interpreted high-level programming language
for general-purpose programming. Created by Guido van Rossum and first
released in 1991, Python has a design philosophy that emphasizes code
readability, notably using significant whitespace.
2962372861@qq.com, 99379321@163.com, cc@i7.com,
0755-8788587, 010-7738780, 0731-88888888"""

n1 = re.findall('(\d+@qq\.com|\d+@163\.com)', str)
print(n1)

n2 = re.findall('(\d\d\d\d-\d\d\d\d\d\d\d|\d\d\d-\d\d\d\d\d\d\d)', str)
print(n2)

n3 = re.findall('(\d{4}-\d{7}|\d{3}-\d{7})', str)
print(n3)

# 替换；
n4 = re.sub('\d', 'AA', str)
print(n4)

# 自定义正则；
#提取电话号码；
t = re.compile('\d{4}-\d{7}|\d{4}-\d{8}|\d{3}-\d{7}|\d{3}-\d{8}')
# 提取电子邮件地址；
m = re.compile('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,4}')
print(t.findall(str))
print(m.findall(str))
