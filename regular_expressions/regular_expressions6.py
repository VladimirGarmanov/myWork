import re
text = text = "Картинка <img src='bg.jpg'> в тексте</p>"
match = re.findall(f'<img.*?>', text)
print(match)