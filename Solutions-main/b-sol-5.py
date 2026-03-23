#formula;f = 9/5 x C + 32

def c2f(celc_input):
    step1 = celc_input*9
    step2 = step1 / 5
    step3_final = step2 + 32

    print(f"{celc_input}°C is {step3_final}°F")

user_input = int(input("What's the temp in °C? :"))
c2f(user_input)