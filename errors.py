# Function to calculate the rounding error
def calculate_error(true_value, decimal_places):
    rounded_value = round(true_value, decimal_places)
    error = abs(rounded_value - true_value)
    return rounded_value, error

def calculate_relative_error(true_value, decimal_places):
    rounded_value, error = calculate_error(true_value, decimal_places)
    relative_error = error / true_value
    return relative_error

def percentage_error(true_value, decimal_places):
    relative_error = calculate_relative_error(true_value, decimal_places)
    percentage_error = relative_error * 100
    return percentage_error

# Input the float number
true_value = float(input("Enter a float number: "))

# Input the number of decimal places to round off
decimal_places = int(input("Enter the number of decimal places to round off: "))

# Calculate the rounded value and error
rounded_value, error = calculate_error(true_value, decimal_places)

# Display the results
print(f"Rounded Value: {rounded_value}")
print(f"Error: {error:.10f}")  # Format the error to display as a normal number

# Calculate the relative error
relative_error = calculate_relative_error(true_value, decimal_places)

# Display the relative error
print(f"Relative Error: {relative_error:.10f}")  # Format the relative error to display as a normal number

# Calculate the percentage error
percentage_error = percentage_error(true_value, decimal_places)

# Display the percentage error
print(f"Percentage Error: {percentage_error:.10f}")  # Format the percentage error to display as a normal number