def calculate_bmi(height, weight):
    """Calculate Body Mass Index (BMI) given height in meters and weight in kilograms."""
    return weight / (height ** 2)

def calculate_bmr(height, weight, age, gender):
    """
    Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation.
    height in cm, weight in kg, age in years
    """
    if gender.lower() == 'male':
        # Formule pour les hommes
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        return round(bmr, 2)
    elif gender.lower() == 'female':
        # Formule pour les femmes
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        return round(bmr, 2)
    else:
        raise ValueError("Gender must be 'male' or 'female'")
