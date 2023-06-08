#Dice Roller Mk4

import random

class DieData:
    #defines the data used for the dice
    def __init__(self, type, sides, count) -> None:
        self.type = type
        self.sides = sides
        self.count = count

    #rolls the die with the set parameters with in the specified count.
    #returns an appended list of integer results
    def dieRoller (self):
        result = []
        while self.count >= 0:
            if self.count != 0:
                self.count -= 1
                dieRoll = random.randint (1, self.sides)
                result.append (dieRoll)
            elif self.count == 0:
                break
        return result
    
    def rollResultSum (self):
        sumofRoll = sum(self.dieRoller())
        return sumofRoll


class RollMod:
    #defines the data used for the modifier
    def __init__(self, type, modval) -> None:
        self.type = type
        self.modval = modval
    #sets the value of the modifier based on parameters
    def rollModifier (self):
        modifier = self.modval
        return modifier
    

#list of results from poolRollManager for final output
listOfRollResults = []
poolTotalResults = []
poolSummedResults = []

#the function that runs the dice pool creation and roll
def poolRollManager ():
    #starts to input sequence. Creates a set of dice for the pool
    addSet = input("Add a set of dice to roll? - Yes or No?")
    if addSet == "Yes":
        #asks for info on hte die that will be put in DieData class
        die_entry = DieData (input ("What type of die is it? Attack, Defense, Red, Green, etc."),
                 int(input("How many sides is the die? - Numbers Only")),
                 int(input("How many dice of this type are being rolled - Numbers Only")))
        #gives the raw result of the dice set rolled
        rawResult = die_entry.dieRoller()
        #creates a list item for the final list of results and adds it to that list
        setRollResult = str(die_entry.type), rawResult
        listOfRollResults.append(setRollResult)
        #adds the raw roll result to a pool for adding - in a list
        poolTotalResults.append(rawResult)
        #sums together the roll result
        summedResults = sum(rawResult)
        #adds the summed result to a list of other summed results of dice rolls
        poolSummedResults.append(summedResults)
        #runs the function again
        poolRollManager()
    elif addSet != "Yes":
        pass

listOfModifiers = []
modListforSum = []

def modifierManager ():
    #asks for information on any modifier that will be put into RollMod class
    modSet = input ("And modifiers? Write 'Yes' or 'No'")
    if modSet == "Yes":
        mod_entry = RollMod (input ("What type of modifier is it? Example: Buff, Boost, Debuff, etc."),
                     int(input("What is the value of the modifier? - Numbers Only")))
        modResult = mod_entry.rollModifier()
        modData = str(mod_entry.type), modResult
        listOfModifiers.append(modData)
        modListforSum.append(modResult)
        modifierManager()
    elif modSet != "Yes":
        pass

def thresholdManager ():
    #this function ask for a challenge threshold and creates a user-inputed value and saves it in a variable.
    include_thres = input ("Include a challenge threshold? Yes or No")
    if include_thres == "Yes":
        threshold_val = int(input("Input the challenge threshold - Numbers Only"))
        return threshold_val
    elif include_thres != "Yes":
        threshold_val = 0
        return threshold_val

#run the roller function    
poolRollManager()
#sum the final results for a final resolved total
poolRollTotal = sum(poolSummedResults)

#run the modifier function
modifierManager()
#sum the modifiers
modifierTotal = sum(modListforSum)

#this variable gets the returned threshold value and holds it for evaluation.
challengeValue = thresholdManager()

#prints each dice set roll that is listed in list of roll results.
print("Dice Pool Rolls:")
for roll_entry in listOfRollResults:
    print(roll_entry)
#prints the dice pool roll total
print ("Dice Pool Total:", poolRollTotal)

#prints each modifer with type and value
print("Modifiers:")
for modifier_entry in listOfModifiers:
    print(modifier_entry)
print("Modifier Total:", modifierTotal)

#prints final resolved total of dice and modifiers
print("Final Results:")
resolvedTotal = poolRollTotal + modifierTotal
print("Resolved Total:", resolvedTotal)

#checks whether there is a challenge and compares it to resolved total if there is and then prints the result.
if challengeValue > 0:
    print ("Challenge Thresehold:", challengeValue)
    if challengeValue < resolvedTotal:
        print ("Roll Succeeded")
    elif challengeValue > resolvedTotal:
        print("Roll Failed")
elif challengeValue <= 0:
    pass
