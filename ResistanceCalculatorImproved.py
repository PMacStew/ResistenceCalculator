resistances = []

resistor_amount = int(input("How many resistors will you be adding? "))
for resistor in range(resistor_amount):
    resistances.append(float(input("What is the resistance of resistor " + str(resistor+1) + "? ")))
