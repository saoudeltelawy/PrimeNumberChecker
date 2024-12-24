app_start = True

# Function to validate user input
def check_user_input(user_input):
    if not user_input.isdigit():  # Validate if input is a digit
        print("Please enter a valid number")
        return False
    else:
        return int(user_input)  # Convert to integer and return

def is_prime_number(num):
    """
    Checks if a given number is a prime number.
    """
    if num <= 1:
        return False
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


# --- Start the App ---
while app_start:
    user_input = input("Enter a number to check if prime or not? ")
    valid_input = check_user_input(user_input)
    if valid_input is not False:
        number = valid_input  # Store the validated integer
        is_prime = is_prime_number(number)  # Use a separate variable for the result
        break


result = "Yes, Prime Number" if is_prime else "No, Not a Prime Number"
print(f"Is {user_input} a prime number? {result}")
