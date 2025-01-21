#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment1B

print("[Ideal Gas Law Calculator]")
moles = float(input("Enter the number of moles of the gas: "))
temperature = float(input("Enter the temperature of the gas in Celsius: "))
volume = float(input("Enter the volume of the gas in Liters: "))
IDEAL_GAS_LAW = float(0.0821)
kelvin = temperature + float(273.15)
top = float(moles * kelvin * IDEAL_GAS_LAW)
pressure = float(top / volume)
rounded_number = round(pressure,2)
rounded_number2 = str(rounded_number)
print("\nThe pressure of the gas is " + rounded_number2 + " atm.")