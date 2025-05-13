# --------------------------
# Input - მომხმარებლისგან მონაცემის მიღება
name = input("Enter your name: ")

# Output - მიღებული მონაცემის დაბეჭდვა
print(f"Hello, {name}!")

# --------------------------

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
concatenated = word1 + " " + word2
print(f"Concatenated words: {concatenated}")

# --------------------------

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
num5 = float(input("Enter the fifth number: "))

average = (num1 + num2 + num3 + num4 + num5) / 5
print(f"The average of the entered numbers is: {average}")

# --------------------------

name = input("Enter your first name: ")
surname = input("Enter your last name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in cm): "))
weight = float(input("Enter your weight (in kg): "))

print(f"My name is {name} {surname}, I am {age} years old, my height is {height} cm, and my weight is {weight} kg.")