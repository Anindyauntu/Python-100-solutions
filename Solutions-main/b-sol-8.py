# Which One is Large?

def whichoneslarge():


    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    num3 = int(input("Enter the third number:"))

    set_of_nums = [num1,num2,num3]
    largest_num = max(set_of_nums)
    counting_if_two_times_any = set_of_nums.count(largest_num)

    if counting_if_two_times_any == 3 :
        print("All numbers are equal.")
    elif counting_if_two_times_any == 2:
        print("Two numbers are equal and the largest, they are both414",largest_num)
    else:
        print(largest_num,"is the largest number.")
    # if num1>num2>num3 :
    #     print(num1,"is the largest number")
    # elif num1>num3>num2 :
    #     print(num1,"is the largest number")
    # elif num2>num1>num3 :
    #     print(num2,"is the largest number")
    # elif num2>num3>num1 :
    #     print(num2,"is the largest number")
    # elif num3>num1>num2 :
    #     print(num3,"is the largest number")
    # else:
    #     print(num3,"is the largest number")

while True:
    whichoneslarge()