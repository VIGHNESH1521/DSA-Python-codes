a = float(input("Enter the first side : "))
b = float(input("Enter the second side : "))
c = float(input("Enter the third side : "))

#Calculate the semi perimeter
s = (a + b + c)/2

#Calculate the area
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area of the Traingle is {}".format(area))