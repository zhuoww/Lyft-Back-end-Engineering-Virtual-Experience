import unittest

from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_array = [1.3,0.6,0.6,0.6]
        tire = OctoprimeTires(tire_wear_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear_array = [0.5,0.5,0.4,0.5]
        tire = OctoprimeTires(tire_wear_array)
        self.assertFalse(tire.needs_service())