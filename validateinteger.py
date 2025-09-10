while True:
    user_input = input("Enter an integer: ")
    if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
        number = int(user_input)
        print("You entered the integer: ", number)
        break
    else:
        print("Invalid input Please enter a valid integer")
