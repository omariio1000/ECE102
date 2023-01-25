A = int(input("Enter a 0 or 1 for A: "))
B = int(input("Enter a 0 or 1 for B "))
C = int(input("Enter a 0 or 1 for C: "))
D = int(input("Enter a 0 or 1 for D: "))

out = (not((A and B) and (C))) and (not(C or not(D)))

if (out == True): print("Out = 1")
else: print("Out = 0")
