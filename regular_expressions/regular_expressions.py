import re
text = 'Еда, беду, победа, ЕДЕ, Еде, беДой, еда'
print(re.findall(pattern=r"[еЕ][дД][ауоеЕ].*", string=text))

