word = input("Input: ")

newword = ""

for c in word:
    if c not in "aeiou" and c not in "AEIOU":
       newword += c

print(newword)
