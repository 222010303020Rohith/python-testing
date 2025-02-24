def greet_by_time():
    user_time = float(input("Enter a time: "))  # Get input from user

    if 7 <= user_time < 12:  # Morning time
        print("Hello, Good morning")
    elif 12 <= user_time < 17:  # Afternoon time
        print("Hello, Good afternoon")
    elif 17 <= user_time < 21:  # Evening time
        print("Hello, Good evening")
    else:  # Night time
        print("Good night")

# Calling the function
greet_by_time()




