text = input('String:')
b = ''
for i in range(len(text)-3,-1,-3):
    b = ' '+text[i:i+3:1] + b
b = text[:len(text)%3]+b
if len(text)%3 == 0:
    b = b.replace(" ","",1)
print(b)