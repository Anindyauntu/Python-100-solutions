def palindrome_num_checker(number):
    string_version = str(number)
    string_version_reversed = int(str(string_version)[::-1])

    if string_version_reversed == number:
        print("Palindrome.")
    else:
        print("Not a Palindrome.")

user_input_num = int(input("Enter your number:"))
palindrome_num_checker(user_input_num)