print("Enter the number of days that we have snow data for: ")
numDays = int(input())

snowList = []
dayIterations = 0

while dayIterations < numDays:
    print(f"How many inches for day {dayIterations + 1}?")
    snowList.append(int(input()))
    dayIterations += 1

print("Snow data entry complete\nChoose the next feature\nEnter 1 to show the day with maximum snow\nEnter 2 to show the with minimum snow\nEnter 3 to show how many days had more snow than a chosen threshold")
featureChosen = int(input())
validInput = False
mostSnow = 0
leastSnow = 0
tooMuchSnow = 0
tooMuchSnowCount = 0
thresholdCount = 0

while validInput == False:
    if featureChosen == 1:
        mostSnow = snowList[0]
        for i in snowList:
            if i > mostSnow:
                mostSnow = i 
        validInput = True
        print(f"Day {snowList.index(mostSnow) + 1} had maximum amount of snow... it had {mostSnow} inches!")

    elif featureChosen == 2:
        leastSnow = snowList[0]
        for i in snowList:
            if i < leastSnow:
                leastSnow = i
        validInput = True
        print(f"Day {snowList.index(leastSnow) + 1} had the minimum amount of snow... it had {leastSnow} inches!")

    elif featureChosen == 3:
        print("How much in inches is too much snow for you?")
        tooMuchSnow = int(input())
        for i in snowList:
            if i >= tooMuchSnow:
                tooMuchSnowCount += 1
        validInput = True
        print(f"You had {tooMuchSnowCount} days with more snow than {tooMuchSnow} inches")

    else:
        print("Thats not a choice, try again")
        featureChosen = int(input())
