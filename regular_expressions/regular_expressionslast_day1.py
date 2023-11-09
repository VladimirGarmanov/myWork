import re
text = 'rabcdeefgyYhFjkIoomnpOeorteeeeetoa'

vowels = 'aeoiuAEOIU'
consonants = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
match = re.findall( string=text, pattern=r'(?:[aeoiuAEOIU]{2,})')
print(match)

