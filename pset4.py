# List comprehension with lambda expression to double numbers in range 1-50
doubled_numbers = [(lambda x: x * 2)(x) for x in range(1, 51)]

# Display the result
print(doubled_numbers)
