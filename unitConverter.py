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
    
    # check if the conversion is between metric or imperial units
    if originalUnit in metricConversionFactors and desiredUnit in metricConversionFactors:
        originalToMeter = metricConversionFactors[originalUnit]
        meter_to_desired = metricConversionFactors[desiredUnit]
    elif originalUnit in imperialConversionFactors and desiredUnit in imperialConversionFactors:
        originalToMeter = imperialConversionFactors[originalUnit]
        meter_to_desired = imperialConversionFactors[desiredUnit]
    elif originalUnit == "pounds" and desiredUnit == "kilo":
        conversionFinal  = 0.453592
    else:
        raise ValueError ("Invalid units.")
    try:
        conversionFinal
    except NameError:
        # Calculate the final conversion factor
        conversionFinal = originalToMeter / meter_to_desired
    # Convert the value from the original unit to the desired unit
    convertedValue = value * conversionFinal
    return convertedValue

originalUnit = input ("Enter the original unit (kilo, deka, meter, deci, centi, milli, micro, nano, pico, feet, inches, pounds): ")
desiredUnit = input ("Enter the desired unit (kilo, deka, meter, deci, centi, milli, micro, nano, pico, feet, inches, pounds): ")
value = float (input ("Enter the value in the original unit: "))

convertedValue = convertUnit (originalUnit, desiredUnit, value)

print(f"{value} {originalUnit} is equal to {convertedValue} {desiredUnit}")
