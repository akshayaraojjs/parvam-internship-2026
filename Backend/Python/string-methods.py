sentence = "My name is Akshay Rao. i like to train students"

# String Methods
# upper()
print(f"Sentence in Uppercase: {sentence.upper()}")

# lower()
print(f"Sentence in Lowercase: {sentence.lower()}")

# title()
print(f"Sentence in Title case: {sentence.title()}")

# swapcase()
print(f"Sentence in Swap case: {sentence.swapcase()}")

# capitalize() - First letter of the word will be uppercase for first sentence
print(f"Sentence in Capitalize: {sentence.capitalize()}")

# Space is considered as a character while counting the index position

# find()
print(f"'a' is found at {sentence.find("a")} position, and 'A' is found at {sentence.find("A")} position")

print(f"Z is found at {sentence.find("Z")}")

# rfind() - find will start from right side
print(f"'a' is found at {sentence.rfind("a")} position, and 'A' is found at {sentence.rfind("A")} position")


# index() will show the index position if it is found, if not found it throws an error, so we can use find method to avoid error
# print(f"Z is found at {sentence.index("Z")}") # error occurs as Z is not found

# rindex() will search from right side but throws error if not found
# print(f"Z is found at {sentence.rindex("Z")}") # error occurs as Z is not found

# count() method is used to find the number of repeatitions of the given substring
print(f"a is repeated for {sentence.count("a")}")
print(f"e is repeated for {sentence.count("e")}")

# startswith() and endswith() methods are used to check the prefix and suffix of the sentence
print(f"Does the Sentence starts with 'My'? {sentence.startswith("My")}")

print(f"Does the Sentence ends with 'students'? {sentence.endswith("students")}")

# len() method is used to check the number of characters in the string
print(f"Number of characters in the given sentence: {len(sentence)}")

# isalpha() - checks whether all characters in the given string in alphabet or not
string = "Akshay"
str1 = "akshay1551"
str2 = "1234"
str3 = "123.4"
print(f"String contains only alpabets: {string.isalpha(), str1.isalpha()}")

# isdigit() - checks whether all characters are numbers (If decimal point found, it will be false)
print(f"String contains only digits: {str1.isdigit(), str2.isdigit(), str3.isdigit()}")

# isdecimal() - checks for the number with decimal point
print(f"String contains decimal value: {str1.isdecimal(), str2.isdecimal(), str3.isdecimal()}") # doubt?

# isalnum() - checks the combination of alphabet and numbers (If any one of the alphabet or number is found, we will get true)
print(f"String contains Alphabets and Numbers: {string.isalnum(), str1.isalnum(), str2.isalnum()}")

# islower() - checks whether all characters are lower case
print(f"akshay is in lowercase, but Akshay is not in lowercase: {"akshay".islower(), "Akshay".islower()}")

# isupper()
print(f"AKSHAY is in uppercase, but Akshay is not in uppercase: {"AKSHAY".isupper(), "Akshay".isupper()}")

# istitle()
print(f"Akshay Rao is in titlecase, but Akshay rao is not in titlecase: {"Akshay Rao".istitle(), "Akshay rao".istitle()}")

# strip() - Used to remove the whitespaces from the string
print(f"  Akshay   :{"  Akshay   ".strip()}")

# lstrip() - Used to remove the whitespaces from the string only on the left side
print(f"  Akshay   :{"  Akshay   ".lstrip()}")

# rstrip() - Used to remove the whitespaces from the string only on the right side
print(f"  Akshay   :{"  Akshay   ".rstrip()}")

# replace() method is used to replace the existing string to another
names = "Akshay Rao brother is Ajay Rao"
print(f"Before Replacing: {names}")
print(f"After Replacinh: {names.replace("Rao", "Kumar")}")

# split() method is used to split the items based on the pattern
names = "Akshay Ajay Akash Vikas Vikram"
print(names.split()) # whitespace is the seperator

# No. of groups to split: split("seperator", limit), groups will be limit + 1
print(names.split(" ", 2)) # comma is the seperator

names = "Akshay,Ajay,Akash,Vikas,Vikram"
print(names.split(",")) # comma is the seperator

namesWithColon = "Akshay-Is-A-Good-Boy"
print(names.split("-"))

# join() method is used to combine the strings
words = ["Hello", "Students", "We", "Shall", "Learn", "Python"]
print(" ".join(words))
print("-".join(words))
print(",".join(words))
print(", ".join(words))
print("".join(words))