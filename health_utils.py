def calculate_bmi(height, weight):
    """Calculate Body Mass Index (BMI) given height in meters and weight in kilograms."""
    return round(weight / (height ** 2), 2)

def calculate_bmr(height, weight, age, gender):
    """
    Calculate Basal Metabolic Rate (BMR) using the Harris-Benedict equation.
    Parameters:
    height: in centimeters
    weight: in kilograms
    age: in years
    gender: 'male' or 'female'
    """
    if gender.lower() == 'male':
        # Formule Harris-Benedict pour les hommes
        bmr = (
            88.362 
            + (13.397 * weight)  # Poids
            + (4.799 * height)   # Taille
            - (5.677 * age)      # Âge
        )
    elif gender.lower() == 'female':
        # Formule Harris-Benedict pour les femmes
        bmr = (
            447.593 
            + (9.247 * weight)   # Poids
            + (3.098 * height)   # Taille
            - (4.330 * age)      # Âge
        )
    else:
        raise ValueError("Gender must be 'male' or 'female'")
    
    return round(bmr, 2)
