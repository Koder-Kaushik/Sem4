def f(x):
    return float(x**3 - 2*x - 5)

def f_derivative(x):
    return float(3*x**2 - 2)  # Derivative of the function f(x)

def newton_raphson():
    x0 = 2.0  # Initial guess
    tolerance = 0.000001
    max_iterations = 100
    iteration = 1

    while True:
        print(f"Iteration {iteration}:")
        fx = f(x0)
        f_prime_x = f_derivative(x0)

        if abs(f_prime_x) < 1e-10:
            print("Derivative is too small. Stopping computation.")
            break

        x1 = x0 - fx / f_prime_x
        print(f"x0 = {x0}, f(x0) = {fx}, f'(x0) = {f_prime_x}, x1 = {x1}")

        if abs(x1 - x0) < tolerance:
            print(f"Root found: {x1}")
            break

        x0 = x1
        iteration += 1

        if iteration > max_iterations:
            print("Maximum iterations reached. Stopping computation.")
            break

def main():
    print("Newton-Raphson Method")
    newton_raphson()

main()