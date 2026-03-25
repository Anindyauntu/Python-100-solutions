def count_digits(num):
    convert = str(num)
    length = len(convert)
    print(f"There are {length} digits in the number.")

user_input_num = int(input("Enter your number:"))
count_digits(user_input_num)