tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."


fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print (fat_cat)

# Testing out escape sequences

print("This sentence makes use of.\b")
print("\U0001F47E")

frmt = "%r"
backslash = "\\"

print(frmt % backslash)