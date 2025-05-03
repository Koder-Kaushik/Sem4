# Gauss Elimination with printed equation format and clear inputs

def gauss_elimination(matrix):
    n = len(matrix)

    # Forward Elimination
    
    for i in range(n):
        for j in range(i+1, n):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(i, n+1):
                matrix[j][k] -= ratio * matrix[i][k]

    # Back Substitution
    x = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = matrix[i][n]
        for j in range(i+1, n):
            x[i] -= matrix[i][j] * x[j]
        x[i] /= matrix[i][i]
    
    return x

# Print equation format and input
print("You will now enter 3 linear equations of the form: a*x + b*y + c*z = d\n")

matrix = []
for i in range(3):
    print(f"Equation {i+1}: a*x + b*y + c*z = d")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))
    matrix.append([a, b, c, d])
    print()

# Solve the system
solution = gauss_elimination(matrix)

# Output
print("Solution:")
variables = ['x', 'y', 'z']
for i in range(3):
    print(f"{variables[i]} = {solution[i]:.4f}")
