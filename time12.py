def is_current():
    time_str = input("Enter a time (HH:MM format, e.g., 07:00, 12:00, 17:00): ")

    if time_str == "07:00":
        print("Hello, good morning")
    elif time_str == "12:00":
        print("Hello, good afternoon")
    elif time_str == "17:00":
        print("Hello, good evening")
    else:
        print("This is not a good time")

# Call the function correctly
is_current()
