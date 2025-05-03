# Jacobi Method - Simplified

def jacobi_method(iterations, eqs):
    # Initial guesses for x, y, z
    x, y, z = 0, 0, 0

    print("\nStarting Jacobi Iterations:\n")
    for itr in range(1, iterations + 1):
        # Update x, y, z based on previous values
        x_new = (eqs[0][3] - eqs[0][1]*y - eqs[0][2]*z) / eqs[0][0]
        y_new = (eqs[1][3] - eqs[1][0]*x - eqs[1][2]*z) / eqs[1][1]
        z_new = (eqs[2][3] - eqs[2][0]*x - eqs[2][1]*y) / eqs[2][2]

        # Display each step
        print(f"Iteration {itr}:")
        print(f"  x = {x_new:.4f}, y = {y_new:.4f}, z = {z_new:.4f}")
        print()

        # Update variables for the next iteration
        x, y, z = x_new, y_new, z_new

    return x, y, z


# Input section
print("Enter the coefficients for 3 equations of the form: ax + by + cz = d\n")
eqs = []
for i in range(3):
    print(f"Equation {i + 1}: a*x + b*y + c*z = d")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))
    eqs.append([a, b, c, d])
    print()

iterations = int(input("Enter number of iterations: "))

# Solve using Jacobi method
x, y, z = jacobi_method(iterations, eqs)

# Output the final result
print("Final Approximate Solution:")
print(f"x = {x:.4f}")
print(f"y = {y:.4f}")
print(f"z = {z:.4f}")
