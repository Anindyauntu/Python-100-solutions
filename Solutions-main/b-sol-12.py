def mul_table(number):
    for i in range(0,11):
        print(number,"x",i,"=",number*i)


user_input = int(input("Enter your number:"))
mul_table(user_input)