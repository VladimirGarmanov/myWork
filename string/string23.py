string = input('String:')
words = 0
listwords = []
for i in range(len(string)):
    if string[i] != ' ':
        words+=1
    if string[i] == ' ' or i == len(string)-1:
        listwords.append(words)
        words = 0

print(max(listwords))