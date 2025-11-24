# pattern_drawing.py

# Prompt the user for the size of the square
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for each row
while row < size:
    # Inner for loop to print '*' size times on the same line
    for col in range(size):
        print("*", end="")
    # Move to the next line after printing a row
    print()
    # Increment the row counter
    row += 1
