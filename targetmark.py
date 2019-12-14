def calculateTargetMark(mm,tp):
    mm=int(mm)
    tp=int(tp)
    tm=mm*(tp/100)
    return tm

while True:
    try:
        #student inputs maximum mark of test
        maxMarks = input("Please enter the maximum mark of the assignment ... ")
        maxmarks = int(maxMarks)

    except(ValueError):
        print("Please enter a valid Base 10 integer")
        continue

    try:
        #student inputs target percentage that they desire
        targetPercent = input("Please enter your target success percentage ... ")
        targetPercent = int(targetPercent)

    except(ValueError):
        print("Please enter a valid Base 10 integer")
        continue

    if targetPercent > 100 or targetPercent <= 0:
        print("Please enter a valid Base 10 Integer between 1 and 100")
        continue

    #calculate number of marks required to achieve student's target percentage
    targetMark=calculateTargetMark(maxMarks,targetPercent)

    #print result
    print(targetMark,"marks out of",maxMarks,"are required to achieve",targetPercent,"%")

    val = input("Would you like to exit? (Y/N) ")

    if val == "y" or val == "Y":
        break
