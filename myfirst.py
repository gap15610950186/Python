from collections import defaultdict
str = input("please input a string:")
str = str.lower()
chars = defaultdict(int)
for char in str:
    chars[char] += 1
new_chars = sorted(chars.items(),key=lambda d:d[1],reverse=True)
print(new_chars)