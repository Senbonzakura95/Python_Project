import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmi(self):
        """Test BMI calculation"""
        height = 1.75  # mètres
        weight = 70    # kg
        expected_bmi = 22.86
        result = calculate_bmi(height, weight)
        self.assertAlmostEqual(result, expected_bmi, places=2)

    def test_calculate_bmr_male(self):
        """Test BMR calculation for males"""
        height = 175  # cm
        weight = 70   # kg
        age = 30      # années
        gender = 'male'
        expected_bmr = 1723.46
        result = calculate_bmr(height, weight, age, gender)
        self.assertAlmostEqual(result, expected_bmr, places=2)

    def test_calculate_bmr_female(self):
        """Test BMR calculation for females"""
        height = 175  # cm
        weight = 70   # kg
        age = 30      # années
        gender = 'female'
        expected_bmr = 1432.79
        result = calculate_bmr(height, weight, age, gender)
        self.assertAlmostEqual(result, expected_bmr, places=2)

if __name__ == '__main__':
    unittest.main()
