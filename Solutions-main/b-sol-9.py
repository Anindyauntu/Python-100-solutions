def check_num_type(num):
    if num > 0:
        return "The number is positive."
    elif num < 0:
        return "The number is negative."
    else:
        return "The number is Zero."

users_number = int(input("Enter your number:"))
result = check_num_type(users_number)
print(result)
