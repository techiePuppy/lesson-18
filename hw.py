def get_valid_age():
    """Prompts the user to enter their age and validates the input.12Handles non-numeric input and negative ages."""
    while True: 
        try:
            age_str = input("Please enter your age: ")
            age = int(age_str)  
            if age < 0:
                print("Age cannot be negative. Please try again.")
            else:
                print(f"Your age is {age}.")
        except ValueError:
            print("Invalid input. Please enter a whole number for your age.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
user_age = get_valid_age()

