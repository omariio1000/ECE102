import math

a = float(input("Enter the value of a (cm): "))
t = float(input("Enter the value of t (mm): "))
L = float(input("Enter the value of L (cm): "))

a = a * 10**-2
t = t * 10**-3

b = a - ((2 * t)/math.tan(math.pi/6))

a = a * 10**2
b = b * 10**2

vol = L * ((a**2 / 2) - (b**2 / 2))
mass = vol * 2.7
mass = mass * 10**-3


print(f"The length of b is {b:.2f} cm")
print(f"The mass of the tube is {mass:.2f} kg")