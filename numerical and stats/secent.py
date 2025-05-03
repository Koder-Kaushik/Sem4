def f(x):
    return float(x**3 - 2*x - 5)

def secant_method():
    x0 = 2.0  # First initial guess
    x1 = 3.0  # Second initial guess
    tolerance = 0.000001
    max_iterations = 100
    iteration = 1

    while True:
        print(f"Iteration {iteration}:")
        f_x0 = f(x0)
        f_x1 = f(x1)

        if abs(f_x1 - f_x0) < 1e-10:
            print("Denominator too small. Stopping computation.")
            break

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        print(f"x0 = {x0}, x1 = {x1}, f(x0) = {f_x0}, f(x1) = {f_x1}, x2 = {x2}")

        if abs(x2 - x1) < tolerance:
            print(f"Root found: {x2}")
            break

        x0, x1 = x1, x2
        iteration += 1

        if iteration > max_iterations:
            print("Maximum iterations reached. Stopping computation.")
            break

def main():
    print("Secant Method")
    secant_method()

main()
