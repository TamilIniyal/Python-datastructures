text = input()
letter = input()
sum = 0
for i in text:
    if letter in i:
        sum = sum + 1
print(sum)
