input_numbers = []
for a in range(4197, 9183):
    if a %5 == 0 and a%6 != 0 and a%10 != 0 and a%13 != 0 and a%16 != 0:
        input_numbers.append(a)
print(len(input_numbers))
print(max(input_numbers))