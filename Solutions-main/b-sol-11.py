def sum_of_num(n):
    step1 = 1 + n
    step2 =  step1 * n
    step3 = step2 / 2
    return int(step3)

user_input_n = int(input("Enter your number(N):"))
print(sum_of_num(user_input_n))