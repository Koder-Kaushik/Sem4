import numpy as np

# Simple Gauss-Seidel Method Implementation
def gauss_seidel(a, b, n):
    # Initialize solution array x with zeros
    x = [0, 0, 0]
    
    print("\nThe solution is:")
    
    # Loop for number of iterations specified
    for iteration in range(n):
        for i in range(3):
            d = b[i]  # Start with the constant term
            
            # Subtract all other terms except the coefficient of the variable
            # we're solving for
            for j in range(3):
                if i != j:
                    d = d - a[i][j] * x[j]
            
            # Divide by the coefficient of the variable to get its value
            x[i] = d / a[i][i]
        
        print(f"Iteration {iteration + 1}:")
        print(f"x = {x[0]:.4f}")
        print(f"y = {x[1]:.4f}")
        print(f"z = {x[2]:.4f}\n")
    
    return x

# Main program
print("Enter the coefficients of the equations:")
print("\nFor equation 1 (ax + by + cz = d)")
a11 = float(input("Enter a: "))
a12 = float(input("Enter b: "))
a13 = float(input("Enter c: "))
b1 = float(input("Enter d: "))

print("\nFor equation 2 (ex + fy + gz = h)")
a21 = float(input("Enter e: "))
a22 = float(input("Enter f: "))
a23 = float(input("Enter g: "))
b2 = float(input("Enter h: "))

print("\nFor equation 3 (ix + jy + kz = l)")
a31 = float(input("Enter i: "))
a32 = float(input("Enter j: "))
a33 = float(input("Enter k: "))
b3 = float(input("Enter l: "))

# Create coefficient matrix and constants vector
a = [[a11, a12, a13],
     [a21, a22, a23],
     [a31, a32, a33]]
b = [b1, b2, b3]

# Number of iterations
iterations = 10

# Get solution
solution = gauss_seidel(a, b, iterations)

print("Final Solution:")
print(f"x = {solution[0]:.4f}")
print(f"y = {solution[1]:.4f}")
print(f"z = {solution[2]:.4f}")

# Verify the solution
print("\nVerifying the solution:")
for i in range(3):
    result = sum(a[i][j] * solution[j] for j in range(3))
    print(f"Equation {i+1}: {result:.4f} ≈ {b[i]}")