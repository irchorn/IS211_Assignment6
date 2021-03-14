import unittest
import conversions
import conversions_refactored
class ConversionFunctions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        celsius = 300
        expected = 573.15
        actual = conversions.convertCelsiusToKelvin(celsius)

        self.assertAlmostEqual(expected, actual, places=2, msg="Celsius to  Kelvin conversion failed")

    def test_convertCelsiusToFahrenheit(self):
        celsius = 300
        expected = 572
        actual = conversions.convertCelsiusToFahrenheit(celsius)
        self.assertAlmostEqual(actual, expected, places=2, msg="Celsius to  Fahrenheit conversion failed")

    def test_convertMilestoYards(self):
        fromUnit = 'Miles'
        toUnit = 'Yards'
        value = 5
        expected = 8800
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Miles to Yards conversion failed")

    def test_convertYardstoMeters(self):
        fromUnit = 'Yards'
        toUnit = 'Meters'
        value = 20
        expected = 18.288
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=3, msg="Yards to Meters conversion failed")

    def test_convert(self):
        fromUnit = 'Celsius'
        toUnit = 'Kelvin'
        value = 10
        expected = 283.15
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(actual, expected, places=2, msg="Celsius to  Kelvin conversion failed")

        fromUnit = 'Celsius'
        toUnit = 'Fahrenheit'
        value = 15
        expected = 59
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(actual, expected, places=2, msg="Celsius to  Fahrenheit conversion failed")

        fromUnit = 'Yards'
        toUnit = 'Meters'
        value = 20
        expected = 18.28
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Yards to Meters conversion failed")

        fromUnit = 'Miles'
        toUnit = 'Yards'
        value = 5
        expected = 8800
        actual = conversions_refactored.convert(fromUnit, toUnit, value)
        self.assertAlmostEqual(expected, actual, places=2, msg="Miles to Yards conversion failed")


if __name__ == '__main__':
    unittest.main()
