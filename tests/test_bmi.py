"""BMI 計算程式的單元測試。"""
import math
import unittest
from BMI import calculate_bmi

class CalculateBMITests(unittest.TestCase):
    def test_reference_cases(self):
        cases = [(60,170,20.76),(45,160,17.58),(90,180,27.78),
                 (62.5,165,22.96),(47.36,160,18.50),(64,160,25.00),
                 (76.8,160,30.00),(100,200,25.00)]
        for weight,height,expected in cases:
            with self.subTest(weight=weight,height=height):
                self.assertAlmostEqual(calculate_bmi(weight,height),expected,delta=0.01)

    def test_rejects_non_positive_values(self):
        for weight,height in [(0,170),(-1,170),(60,0),(60,-170)]:
            with self.subTest(weight=weight,height=height):
                with self.assertRaises(ValueError):
                    calculate_bmi(weight,height)

    def test_rejects_non_numeric_values(self):
        for weight,height in [("abc",170),(60,"abc"),("",170),(60,None)]:
            with self.subTest(weight=weight,height=height):
                with self.assertRaises(ValueError):
                    calculate_bmi(weight,height)

    def test_rejects_non_finite_values(self):
        for value in (math.nan,math.inf,-math.inf):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    calculate_bmi(value,170)
                with self.assertRaises(ValueError):
                    calculate_bmi(60,value)

if __name__ == "__main__":
    unittest.main()
