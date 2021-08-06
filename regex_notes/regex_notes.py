import re

# pattern = r"Cookie"
# sequence = "Cookie"
# if re.match(pattern, sequence):
#     print("Match!")
# else:
#     print("Not a match!")


re.search(r"Co.k.e", "Cookie").group()

# print(re.search(r"^Eat", "Eat cake!").group())

# print(re.search(r"^eat", "Let's eat cake!").group())

# print(re.search(r"cake$", "Cake! Let's eat cake").group())

print(re.search(r"Just a \\sregular character", "Just a \sregular character").group())
