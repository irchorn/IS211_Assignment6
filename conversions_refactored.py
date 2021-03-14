class ConversionNotPossibleException(Exception):
    def __init__(self, message):
        super().__init__(self, message)


def convert(fromUnit, toUnit, value):
    """
    Convert
    """
    if fromUnit == "Celsius" and toUnit == "Kelvin":
        kelvin = celsius + 273.15

    elif fromUnit == "Celsius" and toUnit == "Fahrenheit":
        fahrenheit = (celsius * 1.8) + 32

    elif fromUnit == 'Kelvin' and toUnit == 'Celsius':
        celsius = kelvin - 273.15

    elif fromUnit == 'Kelvin' and toUnit == 'Fahrenheit':
        fahrenheit = (kelvin * 1.8) - 459.67

    elif fromUnit == 'Fahrenheit' and toUnit == 'Kelvin':
        kelvin = (fahrenheit + 459.67) / 1.8

    elif fromUnit == 'Fahrenheit' and toUnit == 'Celsius':
        celsius = (fahrenheit - 32) / 1.8


    elif fromUnit == "Miles" and toUnit == "Yards":
        yards = miles * 1609


    elif fromUnit == "Meters" and toUnit == "Yards":
        meters = yards / 1.094

    else:
        raise ConversionNotPossibleException("Conversion is not possible")