import unittest

from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestLoader):
    def test_needs_service_true(self):
        tire_wear_array = [1.4,0.9,0.6,1.2]
        tire = OctoprimeTire(tire_wear_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear_array = [0.2,0.5,0.4,0.5]
        tire = OctoprimeTire(tire_wear_array)
        self.assertFalse(tire.needs_service())
