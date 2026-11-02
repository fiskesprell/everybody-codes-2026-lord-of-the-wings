import math

silly = [1,2,3,4,5,6,7,8,9,10,11,12,14,16,17,20,24,29,30,32,34,35,39,40,42,43,48,50,51,52,59,60,62,63,67,68,69,70,74,75,76,78,80,83,84,89,90,92,99,100,106,139,196,198,221,224,255,268,274,275,295,296,334,347,366,370,375,378,388,391,400,449,454,466,475,483,518,538,539,566,567,572,583,641,643,647,686,742,762,830,846,871,876,916,922,938,959,977,980,986]

returnNumber = 0

for number in silly:
    squared = number**0.5
    roundUp = math.ceil(squared)
    nextNumber = (roundUp * roundUp)
    nowNeed = (nextNumber - number)

    if (squared.is_integer()):
        print(f"{number} needed 0 pinecones")
    else:
        print(f"square of {number} is {squared}")
        print(f"squared round up = {roundUp}")
        print(f"meaning next number is {nextNumber}")
        print(f"nextnumber: {nextNumber} - original number {number} = {nowNeed}")
        print(f"They therefore need: {nowNeed} number.")
        returnNumber += nowNeed
        print(f"Seeds neded so far: {returnNumber}")


print(f"............................................")
print(f"TOTAL NUTS NEEDED: {returnNumber}")