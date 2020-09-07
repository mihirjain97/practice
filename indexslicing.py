digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
name = "mihir manav"
print(digits[6:1:-3])
print(name[0:])

i = 0
while i < len(digits):
    print(digits[:i])
    i = i+1
print(digits)
for i in range(len(digits)):
    print(digits[:-i-1])
