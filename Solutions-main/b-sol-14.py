def num_reverse(num):
    strlization = int(str(num)[::-1])
    print("Reversed Version:",strlization)


user_input_num = int(input("Enter your number:"))
num_reverse(user_input_num)