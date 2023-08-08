num=input("enter the number")
i = 0
length = len(num)
if (length % 2 == 0):
    length = len(num) + 1

for i in range(length):
    if num[i] != num[-1 - i]:
        print(num, 'is not a Palindrome')
        break
else:
    print(num, 'is a Palindrome')