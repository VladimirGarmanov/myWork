text = input('String:')
for i in range(0, len(text)+len(text) - 1, 2):

    text = text.replace(text[i], f'{text[i]} ')
print(text)