# Odd or Even Identifier ...

def odd_or_even(number):
    victim = number % 2
    if victim == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

user_input_num = int(input("Enter your number:"))
odd_or_even(user_input_num)