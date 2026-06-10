import csv
import os

print("What would you like to do with the Homes file?\nA) Print all file contents\nB) Print (number) first records\nC) Print summary information\nD) Print all house prices for houses that have a price higher than (number)\nE) Print all house information for houses that have (number) bedrooms")
decision = input()
decision = decision[0]
decision = decision.upper()

validInput = False
rowsToPrint = 0
numRecords = 0
mostExpHouse = -1.0
expensiveRow = None
leastExpHouse = float('inf')
cheepRow = None
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
        print("--Summary Information--")

        with open(filePath, mode = "r", encoding = "utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader)

            for row in csvReader:
                if not row or not row[0].strip():
                    continue
                numRecords += 1
                
                currentPrice = float(row[0])

                if currentPrice > mostExpHouse:
                    mostExpHouse = currentPrice
                    expensiveRow = row
                
                if currentPrice < leastExpHouse:
                    leastExpHouse = currentPrice
                    cheepRow = row
        
        print(f"Number of records in the file: {numRecords - 1}\nMost expensive house: {expensiveRow}\nLeast expensive house: {cheepRow}")
        validInput = True

    elif decision == "D":
        with open(filePath, mode = "r", encoding = "utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader)

            print("Enter a price to show all houses more expensive than that")
            userInput = int(input())
            
            for row in csvReader:
                if not row or not row[0].strip():
                    continue
                
                currentPrice = float(row[0])

                if currentPrice > userInput:
                    print(f"${currentPrice}")
        validInput = True

    elif decision == "E":
        with open(filePath, mode = "r", encoding = "utf-8") as file:
            csvReader = csv.reader(file)
            next(csvReader)

            print("Enter the amount of bedrooms you want")
            userInput = int(input())
            
            for row in csvReader:
                if not row or len(row) < 5:
                    continue

                if not row[4].strip():
                    continue
                
                currentBedroom = float(row[4])

                if currentBedroom == userInput:
                    print(f"Info: {row}")
        validInput = True

    else:
        print("Incorect input, try again")
        decision = input()
        decision = decision[0]
        decision = decision.upper()