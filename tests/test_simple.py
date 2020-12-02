import unittest
from unittest.mock import *

from sample.simple import *


class TestSimple(unittest.TestCase):
    def test_needs_fuel_true(self):
        test_object = Car()
        test_object.needs_fuel = Mock(name = 'needs_fuel')
        test_object.needs_fuel.return_value = True

        result = test_object.needs_fuel()
        self.assertEqual(result, True)

    def test_needs_fuel_false(self):
        test_object = Car()
        test_object.needs_fuel = Mock(name = 'needs_fuel')
        test_object.needs_fuel.return_value = False

        result = test_object.needs_fuel()
        self.assertEqual(result, False)

    def test_get_engine_temperature(self):
        test_object = Car()
        test_object.get_engine_temperature = Mock(name = 'get_engine_temperature')
        test_object.get_engine_temperature.return_value = 100

        result = test_object.get_engine_temperature()
        self.assertEqual(result, 100)

    @patch.object(Car, 'drive_to')
    def test_drive_to_destination(self, mock_method):
        test_object = Car()
        dest = 'Sosnowiec'
        mock_method.return_value = 'Drive to Sosnowiec'

        result = test_object.drive_to(dest)
        self.assertEqual(result, 'Drive to Sosnowiec')



if __name__ == '__main__':
    unittest.main()
