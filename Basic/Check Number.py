
def check_number(a):
    if a < 0:
        print("The number you have entered is a negative integer")
    elif a > 0:
        print("The number you have entered is a positive number")
    else:
        print("The number you have entered is zero")

number = float(input("Enter the Number : "))

check_number(number)
