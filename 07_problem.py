'''Temperature Converter Tool
Convert temperatures.
Menu:
1 Celsius → Fahrenheit
2 Fahrenheit → Celsius
3 Exit
Use match-case
Create separate functions for each conversion
Keep running until exit
Concepts used
functions
match-case
loops
variables
arithmetic
F=(C x 9/5)+32'''
def cov_fahrenheit():
    celsius=float(input("Enter degree celsius to convert to Fahrenheit:"))
    f=(celsius*1.8)+32
    print(f)
def cov_celsius():
    fahrenheit=float(input("Enter degree fahrenheit to covert to celsius:"))
    c=(fahrenheit-32)/1.8
    print(c)
while True:
    print("1.convert Celsius to Fahrenheit")
    print("2.convert Fahrenheit to Celsius")
    choice=int(input("Enter number 1 - 3:"))
    match choice:
        case 1:
            cov_fahrenheit()
        case 2:
            cov_celsius()
        case 3:
            print("You exit")
            break
        case _:
            print("Invalid choice")
