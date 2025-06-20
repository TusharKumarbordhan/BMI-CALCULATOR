65

def get_float(prompt):
    """Get a positive float from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("That doesn’t look like a number. Try again.")

def classify_bmi(bmi):
    """Return the BMI category name."""
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obese"

def main():
    print("=== BMI Calculator ===")
    weight = get_float("Enter your weight (kg): ")
    height = get_float("Enter your height (m): ")
    bmi = weight / (height ** 2)
    category = classify_bmi(bmi)

    print(f"\nYour BMI is {bmi:.1f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
