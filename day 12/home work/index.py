num_str = "10"  # სთრინგ რიცხვი
num_int = 5  # integer

# სთრინგის გარდაქმნა integer-ად
num_converted = int(num_str)

# მათემატიკური ოპერაციები
addition = num_converted + num_int
subtraction = num_converted - num_int
multiplication = num_converted * num_int
division = num_converted / num_int

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

height = float(input("Enter your height in cm: "))  # მონაცემთა ტიპის გარდაქმნა
print(f"Data type of height: {type(height)}")  # მონაცემთა ტიპის ბეჭდვა

result = 10 + 5.5  # int + float → Python გარდაქმნის float-ად
print(type(result))  # Output: <class 'float'>

num_str = "100"
num_int = int(num_str)  # Explicit conversion
print(type(num_int))  # Output: <class 'int'>