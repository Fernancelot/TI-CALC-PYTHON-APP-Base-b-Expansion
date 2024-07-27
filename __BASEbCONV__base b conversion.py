# This program implements a function to convert a positive integer to a given base b.
# The function takes two arguments: the integer n and the base b.
# It calculates the base b expansion of the integer n and prints the result.
# The function checks for invalid input values and prints an error message if the input is not valid.
# The base_b_expansion function is then called with user input values to demonstrate the conversion.
# The program can be run and tested with different input values to verify the correctness of the base b expansion.

def base_b_expansion(n, b):
    if b <= 1 or n < 1:
        print("Invalid input. Ensure that b > 1 and n ≥ 1.")
        return
    
    digits = []
    x = n
    while x > 0:
        digits.append(x % b)
        x //= b
    
    # Reverse the list to get the correct order
    digits.reverse()
    
    # Print the digits as a single number
    for digit in digits:
        print(digit, end='')
    print()  # For newline after the result

# Example usage
n = int(input("Enter the integer n (n ≥ 1): "))
b = int(input("Enter the base b (b > 1): "))
base_b_expansion(n, b)
