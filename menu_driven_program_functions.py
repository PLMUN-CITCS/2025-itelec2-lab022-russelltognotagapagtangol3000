def display_menu() -> None:
    """Displays the menu options."""
    print("\nMenu:")
    print("1. Greet User")
    print("2. Check Even/Odd")
    print("3. Exit")


def greet_user() -> None:
    """Prints a greeting message."""
    print("Hello! Welcome!")


def check_even_odd(number: int) -> str:
    """Checks if a number is even or odd and returns the result."""
    return f"{number} is an Even number." if number % 2 == 0 else f"{number} is an Odd number."


def even_odd_checker_action() -> None:
    """Handles input for even/odd check and displays the result."""
    try:
        number = int(input("Enter an integer: "))
        print(check_even_odd(number))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


def handle_menu_choice(choice: int) -> bool:
    """
    Executes actions based on the user's menu choice.
    Returns True if the program should terminate, False otherwise.
    """
    if choice == 1:
        greet_user()
    elif choice == 2:
        even_odd_checker_action()
    elif choice == 3:
        print("Exiting program. Goodbye!")
        return True
    else:
        print("Invalid choice! Please enter a number between 1 and 3.")
    return False


# Main Program Loop
while True:
    display_menu()
    try:
        user_choice = int(input("Enter your choice (1-3): "))
        if handle_menu_choice(user_choice):
            break  # Exit loop if user chooses option 3
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 3.")
