import re
text = 'author=Пушкин А.С.; title = Евгений Онегин; price =200;'

match = re.findall(r"\w+\s*=\s*[^;]+", text)
print(match)