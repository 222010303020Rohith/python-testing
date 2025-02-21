def is_armstrong_number(number):
    num = str(number)  # Convert number to string
    num_digits = len(num)  # Get the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num)  # Armstrong calculation
    return sum_of_powers == number  # Compare with original number
