'''Напишите программу на Python, которая заменяет все вхождения пробела, 
запятой или точки двоеточием.'''

import re
s = input()

pattern = r'[\s,\.]'
print(re.sub(pattern,':',s))