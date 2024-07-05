def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: weight (kg) / (height (m) ** 2)
    """
    bmi = weight / (height ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret the BMI value according to standard categories.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    """
    Main function to run the BMI calculator.
    """
    print("Welcome to the BMI Calculator!")
    
    # Get user input
    weight = float(input("Please enter your weight in kilograms: "))
    height = float(input("Please enter your height in meters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Interpret the BMI value
    category = interpret_bmi(bmi)
    
    # Display the results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are categorized as: {category}")

if __name__ == "__main__":
    main()