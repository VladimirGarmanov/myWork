import re
text = '3.14159625фыпа фцуашгцяразшгРfgfhkjv'
a = re.findall(pattern=r'[^0-9]', string=text)
print(a)
# ^ - исключение того, что есть в квадратных скобках