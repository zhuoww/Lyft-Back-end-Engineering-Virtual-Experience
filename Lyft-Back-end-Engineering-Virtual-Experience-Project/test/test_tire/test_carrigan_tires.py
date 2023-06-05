import unittest

from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_array = [0.3,0.9,0.6,1.2]
        tire = CarriganTires(tire_wear_array)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear_array = [0.4,0.5,0.8,0.5]
        tire = CarriganTires(tire_wear_array)
        self.assertFalse(tire.needs_service())