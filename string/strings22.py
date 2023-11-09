string = input('String:')
words = 1
for i in range(len(string)):
    if string[i] == ' ':
        words+=1
    if string[i-1] == ' ' and string[i] == ' ':
        words-=1

print(words)