def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / height^2 (m^2)
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    # Categories based on BMI values
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def convert_to_meters(feet, inches):
    # Convert height in feet and inches to meters
    total_inches = feet * 12 + inches
    return total_inches * 0.0254  # 1 inch = 0.0254 meters

# Input from user
weight = float(input("Enter your weight in kilograms: "))
feet = int(input("Enter your height in feet: "))
inches = int(input("Enter your height in inches: "))

# Convert height to meters
height_in_meters = convert_to_meters(feet, inches)

# Calculate BMI
bmi = calculate_bmi(weight, height_in_meters)

# Output results
print(f"Your BMI is: {bmi:.2f}")
print(f"You are classified as: {bmi_category(bmi)}")
