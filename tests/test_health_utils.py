def test_calculate_bmr_male(self):
    """Test BMR calculation for males"""
    height = 175  # cm
    weight = 70   # kg
    age = 30      # années
    gender = 'male'
    expected_bmr = 1695.67  # Modifié
    result = calculate_bmr(height, weight, age, gender)
    self.assertAlmostEqual(result, expected_bmr, places=2)

def test_calculate_bmr_female(self):
    """Test BMR calculation for females"""
    height = 175  # cm
    weight = 70   # kg
    age = 30      # années
    gender = 'female'
    expected_bmr = 1507.13  # Modifié
    result = calculate_bmr(height, weight, age, gender)
    self.assertAlmostEqual(result, expected_bmr, places=2)