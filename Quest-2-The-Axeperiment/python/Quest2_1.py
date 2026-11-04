"""

Yeah, the "algorithm" i spent 10 minutes on yesterday has reached its logical conclusion.
Spoiler-alert: it does not work.
This is only uploaded to document for myself that 
"Yes, i programmed something 04/11/2026. Was it good? No. Did i do something? Yes."
Thanks for reading my blog post.

TODO:
    Delete everything here
    Actually think
    Try again



xmy_notes = 
    3<2 2>4 4<1 1<3 4<5 5<2 5>1 2>1 4<3 3>5
    4>3 1<5 1<4 3>1 1<2 2<3 2<5 4<5 5>3 4>2
    4>1 4<5 2>1 4>2 5>1 3>5 5>2 3>2 3>1 4<3
    5>2 2>1 5>3 1<5 4<2 1>3 4>3 4<5 3<2 4>1
    1>4 5<2 5>4 3>5 1<2 2>3 1>5 3>1 4<3 4<2
    4<1 5<2 3>5 1<2 3>1 5<1 2>4 5<4 3>2 3>4
    2>1 5>2 3>1 1<5 3<2 4>2 4<5 1<4 3<4 3<5
    5<1 2>5 4>1 5<3 2<4 4>3 1<2 4>5 3>1 2>3
    5>4 1<2 1<3 3>5 2<4 2<3 1<5 1<4 4<3 5>2
    1<2 2>4 1<3 2>3 2>5 4>3 5>1 5<4 4>1 5>3

    # 35124
    # 43521
    # 43512
"""

my_notes = "4<3 2<5 3>1 1>2 1<5 4<1 3>2 4<2 3>5 4<5 4>1 2>1 3>2 1<5 4>5 2<5 3>1 4>3 2<4 5<3 5>1 5>2 4>1 2<4 3>2 3<4 1>2 3>5 1<3 4>5"

numA = "X"
numB = "X"
operator = "X"
currentChecksum = ["1", "2"]
finalChecksum = 0
iterator = 0 # Reset iterator and currentChecksum after 40 iterations (do not include spaces in iterations)


# Reset variables after (left/right)Bigger is called
def resetVars():
    numA = "X"
    numB = "X"
    operator = "X"

def leftBigger():
    if (numB in currentChecksum) == False and (numA in currentChecksum) == False:
        currentChecksum.append(numA)
        currentChecksum.append(numB)
    elif (numB in currentChecksum) == True and (numA in currentChecksum) == False:
        bIndex = currentChecksum.index(numB)
        currentChecksum.insert(bIndex, numA)
    elif (numB in currentChecksum) == False and (numA in currentChecksum) == True:
        currentChecksum.append(numB)
    elif (numB in currentChecksum) == True and (numA in currentChecksum) == True:
        if (currentChecksum.index(numB) < currentChecksum.index(numA)): 
            # if numA is placed more to the right (it needs to be left if it is bigger)
            currentChecksum.remove(numA)
            currentChecksum.insert(currentChecksum.index(numB), numA)
    else:
        print("Bro there was an error idk what to tell you. Yeah, in leftBigger(). Fix it.")



def rightBigger():
    if (numA in currentChecksum) == False and (numB in currentChecksum) == False:
        currentChecksum.append(numB)
        currentChecksum.append(numA)
    elif (numA in currentChecksum) == True and (numB in currentChecksum) == False:
        aIndex = currentChecksum.index(numA)
        currentChecksum.insert(aIndex, numB) 
    elif (numA in currentChecksum) == False and (numB in currentChecksum) == True:
        currentChecksum.append(numA)
    elif (numA in currentChecksum) == True and (numB in currentChecksum) == True:
        if (currentChecksum.index(numA) < currentChecksum.index(numB)): 
            # if numB is placed more to the right (it needs to be left if it is bigger)
            currentChecksum.remove(numB)
            currentChecksum.insert(currentChecksum.index(numA), numB)
    else:
        print("Bro there was an error idk what to tell you. Yeah, in rightBigger(). Fix it.")

def rowFinished(current_checksum):

    returnValue = int("".join(map(str, current_checksum))) #found on geeksforgeeks, thanks buddy.
    
    iterator = 0
    currentChecksum = ["1", "2"]

    print(returnValue)
    return returnValue

for character in my_notes:
    if character == " ":
        continue
    elif numA == "X":
        numA = character
    elif operator == "X":
        operator = character
    elif numB == "X":
        numB = character
    else:
        if operator == ">":
            leftBigger()
            resetVars()
        else: 
            rightBigger()
            resetVars()
    
    if iterator > 40:
        finalChecksum += rowFinished(currentChecksum)
    else:
        iterator += 1


print(finalChecksum)
        
        
    
"""
    Terrible implementation made in 10 minutes (there is !!DEFINITELY!! a better way to do this lol.)
    Need to do:
    - finish logic of leftBigger & rightBigger.
        - using leftBigger as example:
            Go through all numbers in currentChecksum -> check if left(numA) is more to the left than right(numB)
            if more to the left: do nothing
            if more to the right: place numA directly to left of numB
    - call resetVars() once numA, numB and operator is filled -> after left/rightBigger is called
    - once 40 characters are parsed -> turn currentChecksum into proper number (eg. 53421) -> add that to finalChecksum, reset 0-40 iterator.
    - once all character in my_notes are parsed -> print(finalChecksum)

    should work? (no.)
"""