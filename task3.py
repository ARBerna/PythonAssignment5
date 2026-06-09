import csv
import os

print("What would you like to do with the Homes file?\nA) Print all file contents\nB) Print (number) first records\nC) Print summary information\nD) Print all house prices for houses that have a price higher than (number)\nE) Print all hhouse information for houses that have (number) bedrooms")
decision = input()
decision = decision[0]
decision = decision.upper()

validInput = False
rowsToPrint = 0
scriptDir = os.path.dirname(__file__)
filePath = os.path.join(scriptDir, "task2", "homes.csv")

while validInput == False:
    if decision == "A":
        with open(filePath, mode = "r", encoding = "utf-8") as file:
            csvReader = csv.reader(file)
            for row in csvReader:
                print(row)
        validInput = True
    elif decision == "B":
        print("How many rows would you like to print?")
        rowsToPrint = int(input())

        with open(filePath, mode = "r", encoding = "utf-8") as file:
            csvReader = csv.reader(file)
            for row in range(rowsToPrint + 1):
                print(next(csvReader))
        validInput = True

    elif decision == "C":
        validInput = True

    elif decision == "D":
        validInput = True

    elif decision == "E":
        validInput = True

    else:
        print("Incorect input, try again")
        decision = input()
        decision = decision[0]
        decision = decision.upper()