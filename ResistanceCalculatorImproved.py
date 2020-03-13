from time import sleep

# initial instructions
print("Welcome to the Resistance Calculator! Here is how it works:" + "\n" +
      "You will fist be prompted to enter how many resistors you are using in total. Then you will need to give "
      "a value, in Ohms, for each of the resistors." + "\n" +
      "Next, you will need to specify which resistors you want to add together, step by step. You will also need "
      "to say whether the chunk is to be added in parallel, or in series." + "\n" +
      "Each \"chunk\" of resistors, after being added together, will be saved as the lowest of those "
      "resistor that were added." + "\n" +
      "For example, if I add resistor 3 and resistor 4 and get 16 Ohms, 16 ohms would be the new value for "
      "resistor 3 and resistor 4 would no longer exist." + "\n" +
      "Have fun!" + "\n")
sleep(3)

# program start
resistances = []  # list that will contain all resistors and their values
is_done_adding = False

resistor_amount = int(input("How many resistors will you be adding? "))  # how many resistors are in the mixed circuit?
for resistor in range(resistor_amount):
    resistances.append(float(input("What is the resistance of resistor " + str(resistor + 1) + "? ")))
    # add resistor items to the list
while not is_done_adding:
    circuit_type = input("Will you be adding in series or in parallel? (type \'P\' for parallel and \'S\' for series) ")


def add_series(resistors):
    total = 0
    for i in range(resistors):
        total += resistors[i]
    return total


def add_parallel(resistors):
    total = 0
    for i in range(resistors):
        total += 1 / resistors[i]
    return 1/total
