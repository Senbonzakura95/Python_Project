import unittest
from health_utils import calculate_bmi, calculate_bmr

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)

    def test_calculate_bmr_male(self):
        # Test avec les valeurs exactes de la formule
        result = calculate_bmr(175, 70, 30, 'male')
        self.assertAlmostEqual(result, 1723.46, places=2)

    def test_calculate_bmr_female(self):
        # Test avec les valeurs exactes de la formule
        result = calculate_bmr(175, 70, 30, 'female')
        self.assertAlmostEqual(result, 1432.79, places=2)

if __name__ == '__main__':
    unittest.main()
