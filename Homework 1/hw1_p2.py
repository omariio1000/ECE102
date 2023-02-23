v = 100
r1 = 1000
r2 = 500
r3 = 3000
r4 = 150
r5 = 75
r6 = 100
r7 = 100
r8 = 220

#part a
rTotal = 1/((1/(r1 + r8)) + (1/(r2 + (1/((1/(r5 + r6)) + (1/(r3 + r4)))) + r7)))
print(f"The total resistance is {rTotal:.2f}\u2126")

#part b
i = v/rTotal
print(f"The current at a is {i:.2f}A")

#part c
v220 = (r8/(r1 + r8)) * v
print(f"The voltage drop accross the 220\u2126 resistor is {v220:.2f}V")

#part d
i765 = v/(1/(1/(r2 + (1/((1/(r5 + r6)) + (1/(r3 + r4)))) + r7)))
v165 = i765 * (1/((1/(r5 + r6)) + (1/(r3 + r4))))
i75 = v165 / (r5 + r6)
print(f"The current in the 75\u2126 resistor is {i75:.2f}A")

#part e
pR7 = (i75 ** 2) / v
print(f"The power dissipated by resistor R\u2087 is {pR7:.2e}W")