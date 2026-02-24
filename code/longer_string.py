string1 = (input("Please type in string 1: "))
string2 = (input("Please type in string 2: "))

len1 = len(string1)
len2 = len(string2)

if len1 > len2:
    print(f"{string1} is longer")
elif len1 < len2:
    print(f"{string2} is longer")
else:
    print("The strings are equally long")

# ---- Model Solution ----
#
# input_string1 = input("Please type in string 1: ")
# input_string2 = input("Please type in string 2: ")
#  
# if len(input_string1) > len(input_string2):
#     print(input_string1, "is longer")
# elif len(input_string2) > len(input_string1):
#     print(input_string2, "is longer")
# else:
#     print("The strings are equally long")
