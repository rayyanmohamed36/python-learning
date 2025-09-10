log_file = "user_logs.txt"

print("Type your messages. Type 'exit' to quit.")

while True:
    user_input = input("Enter message: ")
    
    if user_input.lower() == "exit":
        print("Exiting")
        break
    

    with open(log_file, "a") as file:
        file.write(user_input + "\n")
    
    print("logged")
