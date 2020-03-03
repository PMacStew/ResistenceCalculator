# Different resistor variables
resistor1 = 1
resistor2 = 2
resistor3 = 3
resistor4 = 4
resistor5 = 5
resistor6 = 6
resistor7 = 7
resistor8 = 8
resistor9 = 9
resistor10 = 10


def adding_resistor_assignment():
    global adding_resistor
    global adding_resistor_ohm
    if adding_resistor == resistor1:
        adding_resistor_ohm = resistor1_ohm
    elif adding_resistor == resistor2:
        adding_resistor_ohm = resistor2_ohm
    elif adding_resistor == resistor3:
        adding_resistor_ohm = resistor3_ohm
    elif adding_resistor == resistor4:
        adding_resistor_ohm = resistor4_ohm
    elif adding_resistor == resistor5:
        adding_resistor_ohm = resistor5_ohm
    elif adding_resistor == resistor6:
        adding_resistor_ohm = resistor6_ohm
    elif adding_resistor == resistor7:
        adding_resistor_ohm = resistor7_ohm
    elif adding_resistor == resistor8:
        adding_resistor_ohm = resistor8_ohm
    elif adding_resistor == resistor9:
        adding_resistor_ohm = resistor9_ohm
    elif adding_resistor == resistor10:
        adding_resistor_ohm = resistor10_ohm


def first_resistor_assignment():
    global first_resistor_number
    global first_resistor_ohm
    if first_resistor_number == resistor1:
        first_resistor_ohm = resistor1_ohm
    elif first_resistor_number == resistor2:
        first_resistor_ohm = resistor2_ohm
    elif first_resistor_number == resistor3:
        first_resistor_ohm = resistor3_ohm
    elif first_resistor_number == resistor4:
        first_resistor_ohm = resistor4_ohm
    elif first_resistor_number == resistor5:
        first_resistor_ohm = resistor5_ohm
    elif first_resistor_number == resistor6:
        first_resistor_ohm = resistor6_ohm
    elif first_resistor_number == resistor7:
        first_resistor_ohm = resistor7_ohm
    elif first_resistor_number == resistor8:
        first_resistor_ohm = resistor8_ohm
    elif first_resistor_number == resistor9:
        first_resistor_ohm = resistor9_ohm
    elif first_resistor_number == resistor10:
        first_resistor_ohm = resistor10_ohm


def equations():
    global final
    global first_resistor_ohm
    global first_resistor_number
    global resistor1
    global adding_resistor
    global series_parallel
    global resistor1
    global resistor2
    global resistor3
    global resistor4
    global resistor5
    global resistor6
    global resistor7
    global resistor8
    global resistor9
    global resistor10
    global resistor1_ohm
    global resistor2_ohm
    global resistor3_ohm
    global resistor4_ohm
    global resistor5_ohm
    global resistor6_ohm
    global resistor7_ohm
    global resistor8_ohm
    global resistor9_ohm
    global resistor10_ohm
    if (adding_resistor == resistor1 or first_resistor_number == resistor1) and series_parallel == 1:
        resistor1_ohm = adding_resistor_ohm + first_resistor_ohm
        final = resistor1_ohm
    elif (adding_resistor == resistor2 or first_resistor_number == resistor2) and series_parallel == 1:
        resistor2_ohm = adding_resistor_ohm + first_resistor_ohm
        final = resistor2_ohm
    elif (adding_resistor == resistor3 or first_resistor_number == resistor3) and series_parallel == 1:
        resistor3_ohm = adding_resistor_ohm + first_resistor_ohm
        final = resistor3_ohm
    elif (adding_resistor == resistor4 or first_resistor_number == resistor4) and series_parallel == 1:
        resistor4_ohm = adding_resistor_ohm + first_resistor_ohm
        final = resistor4_ohm
    elif (adding_resistor == resistor5 or first_resistor_number == resistor5) and series_parallel == 1:
        resistor5_ohm = adding_resistor_ohm + first_resistor_ohm
        final = resistor5_ohm
    elif (adding_resistor == resistor6 or first_resistor_number == resistor6) and series_parallel == 1:
        resistor6_ohm = adding_resistor_ohm + first_resistor_ohm
        final = resistor6_ohm
    elif (adding_resistor == resistor7 or first_resistor_number == resistor7) and series_parallel == 1:
        resistor7_ohm = adding_resistor_ohm + first_resistor_ohm
        final = resistor7_ohm
    elif (adding_resistor == resistor8 or first_resistor_number == resistor8) and series_parallel == 1:
        resistor8_ohm = adding_resistor_ohm + first_resistor_ohm
        final = resistor8_ohm
    elif (adding_resistor == resistor9 or first_resistor_number == resistor9) and series_parallel == 1:
        resistor9_ohm = adding_resistor_ohm + first_resistor_ohm
        final = resistor9_ohm
    elif (adding_resistor == resistor10 or first_resistor_number == resistor10) and series_parallel == 1:
        resistor10_ohm = adding_resistor_ohm + first_resistor_ohm
        final = resistor10_ohm

    # This id for in parallel

    elif (adding_resistor == resistor1 or first_resistor_number == resistor1) and series_parallel == 2:
        resistor1_ohm = (adding_resistor_ohm * first_resistor_ohm) / (adding_resistor_ohm + first_resistor_ohm)
        final = resistor1_ohm
    elif (adding_resistor == resistor2 or first_resistor_number == resistor2) and series_parallel == 2:
        resistor2_ohm = (adding_resistor_ohm * first_resistor_ohm) / (adding_resistor_ohm + first_resistor_ohm)
        final = resistor2_ohm
    elif (adding_resistor == resistor3 or first_resistor_number == resistor3) and series_parallel == 2:
        resistor3_ohm = (adding_resistor_ohm * first_resistor_ohm) / (adding_resistor_ohm + first_resistor_ohm)
        final = resistor3_ohm
    elif (adding_resistor == resistor4 or first_resistor_number == resistor4) and series_parallel == 2:
        resistor4_ohm = (adding_resistor_ohm * first_resistor_ohm) /(adding_resistor_ohm + first_resistor_ohm)
        final = resistor4_ohm
    elif (adding_resistor == resistor5 or first_resistor_number == resistor5) and series_parallel == 2:
        resistor5_ohm = (adding_resistor_ohm * first_resistor_ohm) / (adding_resistor_ohm + first_resistor_ohm)
        final = resistor5_ohm
    elif (adding_resistor == resistor6 or first_resistor_number == resistor6) and series_parallel == 2:
        resistor6_ohm = (adding_resistor_ohm * first_resistor_ohm) / (adding_resistor_ohm + first_resistor_ohm)
        final = resistor6_ohm
    elif (adding_resistor == resistor7 or first_resistor_number == resistor7) and series_parallel == 2:
        resistor7_ohm = (adding_resistor_ohm * first_resistor_ohm) / (adding_resistor_ohm + first_resistor_ohm)
        final = resistor7_ohm
    elif (adding_resistor == resistor8 or first_resistor_number == resistor8) and series_parallel == 2:
        resistor8_ohm = (adding_resistor_ohm * first_resistor_ohm) / (adding_resistor_ohm + first_resistor_ohm)
        final = resistor8_ohm
    elif (adding_resistor == resistor9 or first_resistor_number == resistor9) and series_parallel == 2:
        resistor9_ohm = (adding_resistor_ohm * first_resistor_ohm) / (adding_resistor_ohm + first_resistor_ohm)
        final = resistor9_ohm
    elif (adding_resistor == resistor10 or first_resistor_number == resistor10) and series_parallel == 2:
        resistor10_ohm = (adding_resistor_ohm * first_resistor_ohm) / (adding_resistor_ohm + first_resistor_ohm)
        final = resistor10_ohm


# How many resistors will you use
resistor_amount = int(input("How many resistor will you be adding? "))
for i in range(resistor_amount):
    resistor_number = i + 1
    if resistor_number == resistor1:
        resistor1_ohm = float(input("What is the value of resistor " + str(resistor_number) + ": "))
    if resistor_number == resistor2:
        resistor2_ohm = float(input("What is the value of resistor " + str(resistor_number) + ": "))
    if resistor_number == resistor3:
        resistor3_ohm = float(input("What is the value of resistor " + str(resistor_number) + ": "))
    if resistor_number == resistor4:
        resistor4_ohm = float(input("What is the value of resistor " + str(resistor_number) + ": "))
    if resistor_number == resistor5:
        resistor5_ohm = float(input("What is the value of resistor " + str(resistor_number) + ": "))
    if resistor_number == resistor6:
        resistor6_ohm = float(input("What is the value of resistor " + str(resistor_number) + ": "))
    if resistor_number == resistor7:
        resistor7_ohm = float(input("What is the value of resistor " + str(resistor_number) + ": "))
    if resistor_number == resistor8:
        resistor8_ohm = float(input("What is the value of resistor " + str(resistor_number) + ": "))
    if resistor_number == resistor9:
        resistor9_ohm = float(input("What is the value of resistor " + str(resistor_number) + ": "))
    if resistor_number == resistor10:
        resistor10_ohm = float(input("What is the value of resistor " + str(resistor_number) + ": "))
# Will you be adding in series or parallel
for j in range(resistor_amount - 1):
    resistor_number = j + 2
    if resistor_number >= 2:
        first_resistor_number = int(input("What resistor would you like to add: "))
        adding_resistor = int(
            input("Which resistor would you like to add resistor " + str(first_resistor_number) + " to: "))
        print("If in series type s. If in parallel type p.")
        series_parallel_real = str(input("Would you like to add resistor " + str(resistor_number) + " to resistor " + str(
            adding_resistor) + " in parallel or in series: "))
        if series_parallel_real == 's' or'S':
            series_parallel = 1
        elif series_parallel_real == 'p' or 'P':
            series_parallel = 2
        else:
            print("Invalid answer")
        adding_resistor_assignment()
        first_resistor_assignment()
        equations()
print("Your overall resistance is: " + str(final))
