"""
unitConverter.py
Ashley Ung
This program will prompt the user to input the original unit, desired unit, and value in the original unit. It will then use the conversion factors to convert the value to the desired unit and print the result.
"""
    
def convertUnit (originalUnit, desiredUnit, value):
    metricConversionFactors = {
        "kilo": 1000,
        "deka": 10,
        "meter": 1,
        "deci": 0.1,
        "centi": 0.01,
        "milli": 0.001,
        "micro": 0.000001,
        "nano": 0.000000001,
        "pico": 0.000000000001
    }
    imperialConversionFactors = {
        "feet": 0.3048,
        "inches": 0.0254,
        "pounds": 0.453592
    }
