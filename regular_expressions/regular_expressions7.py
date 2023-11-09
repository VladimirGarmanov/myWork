import re
text = "uydsfgfkd<img src='путь к картинке'> gdzfdfgz"
match = re.findall(r'<img\s+[^<]*?src\s*=\s*[^>]*>', text)
print(match)