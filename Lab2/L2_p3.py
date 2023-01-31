import numpy as np
import matplotlib.pyplot as plt
import math

def prompt():
    mass = -1.0
    while (mass < 0):
        print("Enter mass of the object (kg): ", end="")
        mass = float(input())
        if (mass < 0): print("Error: Mass must be positive.")
    
    height = -1.0
    while (height < 0):
        print("Enter height of the object (m): ", end="")
        height = float(input())
        if (height < 0): print("Error: Height must be positive.")

    num_pts = -1
    while ((num_pts < 2) | (num_pts > 100)):
        print("Enter number of height points: ", end="")
        num_pts = int(input())
        if ((num_pts < 2) | (num_pts > 100)): print("Error: Invalid number of points.")

    return (mass, height, num_pts)
       
def calcArrays(mass:float, height:np.ndarray):
    pe = mass * height * 9.81
    v = np.zeros(len(height))
    for i in range(len(height)):
        v[i] = math.sqrt((pe[i] * 2) / mass)
    return (pe, v)

def printTable(h:np.ndarray, p:np.ndarray, v:np.ndarray):
    print("{:>10}{:>10}{:>10}".format('h', 'Ei', 'vF'))
    for i in range(len(h)):
        print("{:>10.2f}{:>10.2f}{:>10.2f}".format(h[i], p[i], v[i]))
        #print ("%.2f\t%.2f\t%.2f" % (h[i], p[i], v[i]))
    return

def plot(h:np.ndarray, p:np.ndarray, v:np.ndarray, m:float):
    fig, (ax1, ax2) = plt.subplots(1, 2)
    
    ax1.plot(h, p, color='r')
    ax2.plot(h, v, color='b')

    ax1.grid()
    ax2.grid()

    ax1.set_title(label='Potential Energy vs. Height\nObject Mass = %f kg' % m)
    ax2.set_title(label='Velocity vs. Height\nObject Mass = %f kg' % m)
    
    ax1.set_xlabel('Height h (m)')
    ax2.set_xlabel('Height h (m)')

    ax1.set_ylabel('Energy Ei (J)')
    ax2.set_ylabel('Velocity v (m/s)')

    plt.show()
    return

def main():
    mass, height, num_pts = prompt()
    height_vals = np.linspace(0, height, num_pts)
    pe, v = calcArrays(mass, height_vals)
    printTable(height_vals, pe, v)
    plot(height_vals, pe, v, mass)

if __name__ == "__main__":
    main()