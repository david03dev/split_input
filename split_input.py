# Function to print even and odd digits of a number in ascending order
def print_even_odd_digits(number):
    even_digits = []
    odd_digits = []
    
    # Convert number to string to iterate through each digit
    num_str = str(number)
    
    for digit_char in num_str:
        digit = int(digit_char)
        if digit % 2 == 0:
            even_digits.append(digit)
        else:
            odd_digits.append(digit)
    
    # Sort even and odd digits in ascending order
    even_digits.sort()
    odd_digits.sort()
    
    # Print even digits
    print("Even digits:", end=" ")
    if even_digits:
        print(*even_digits)
    else:
        print("None")
    
    # Print odd digits
    print("Odd digits:", end=" ")
    if odd_digits:
        print(*odd_digits)
    else:
        print("None")

# Reading input
print("Enter an integer:")
input_number = int(input().strip())  # Read input and convert to integer

# Call function to print even and odd digits in ascending order
print_even_odd_digits(input_number)
