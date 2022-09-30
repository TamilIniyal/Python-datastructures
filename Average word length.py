text = input()
s = text.split()
c = text.count(" ")
l = len(text)
letters = l - c
sum = 0
for i in s:
    sum = sum + 1
length = letters/sum
print(length)
