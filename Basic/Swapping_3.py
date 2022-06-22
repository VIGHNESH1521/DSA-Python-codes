P = int(input("Please enter value for P: "))
Q = int(input("Please enter value for Q: "))

# To Swap the values of two variables using XOR
P = P ^ Q
Q = P ^ Q
P = P ^ Q

print("The Value of P and Q after swapping using a XOR operator are {} and {}: ".format(P, Q))