#Dice Roller Graphical
from tkinter import *

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
        while self.count > 0:
            self.count -= 1
            dieRoll = random.randint (1, self.sides)
            result.append (dieRoll)

        return result


class RollMod:
    #defines the data used for the modifier
    def __init__(self, type, modval) -> None:
        self.type = type
        self.modval = modval
    #sets the value of the modifier based on parameters
    def rollModifier (self):
        modifier = self.modval
        return modifier


singleDiceSet = {}
totalPoolOfDice = []
listOfDiceSets = []

#this function control the addition and clearing of the dicepool
def poolManager (status):
    #when the add dice pool button is clicked, data from the entry fields will taken and put into the dicepool window
    #and added to an dicepool list for rolling.
    if status == "Add":
        dicePool = []

        singleDiceSet ['Type'] = str(dieEntryField.get())
        dicePool.append(str(dieEntryField.get()))

        singleDiceSet ['Sides'] = int(dieSideEntry.get())
        dicePool.append(int(dieSideEntry.get()))

        singleDiceSet ['Count'] = int(dieCountEntry.get())
        dicePool.append(int(dieCountEntry.get()))

        totalPoolOfDice.append(dicePool)

        diceDetails = str(singleDiceSet ['Count']), singleDiceSet ['Type'] + " Dice", str(singleDiceSet ['Sides']) + " Sides" 

        dicePoolEntryLabel = Label(poolDataFrame, text= diceDetails)
        dicePoolEntryLabel.pack(side=TOP, padx=5, pady=5)

        dieEntryField.delete(0, END)
        dieSideEntry.delete(0, END)
        dieCountEntry.delete(0, END)
    
    #when the clear pool button is clicked, the labels with the details on each dice set in the dice pool window are cleared.
    #the interal lists which hold each dice set is also cleared for new entries.
    if status == "Clear":
        totalPoolOfDice.clear()
        singleDiceSet.clear()
        def clear_poolFrame():
            for widgets in poolDataFrame.winfo_children():
                widgets.destroy()
        clear_poolFrame()

singleModSet = {}
listOfModifiers = []
totalModList = []
modListforSum = []

def modManager (status) :
    if status == "Add":
        modset = []

        singleModSet ['Type'] = str(modNameEntry.get())
        modset.append(str(modNameEntry.get()))

        singleModSet ['Value'] = int(modValEntry.get())
        modset.append(int(modValEntry.get()))

        listOfModifiers.append(modset)

        modDetails = str(singleModSet ['Type']), str(singleModSet ['Value'])
        modifierDetailLable = Label(modDataFrame, text=modDetails)
        modifierDetailLable.pack(side=TOP, padx=5, pady=5)

        modNameEntry.delete(0, END)
        modValEntry.delete(0, END)

    if status == "Clear":
        listOfModifiers.clear()
        singleModSet.clear()
        def clear_modDataFrame():
            for widgets in modDataFrame.winfo_children():
                widgets.destroy()
        clear_modDataFrame()


#function that activates when roll button is clicked
def clickRollButton ():
    listOfDiceSets.clear()
    for sets in totalPoolOfDice:
       die_set = DieData (sets[0], sets[1],sets[2])
       rawResult = die_set.dieRoller()
       setRollResult = str(die_set.type), rawResult
       listOfDiceSets.append(setRollResult)
    
    totalModList.clear()
    for modSets in listOfModifiers:
        the_modifier = RollMod (modSets[0], modSets[1])
        modListforSum.append(the_modifier.modval)
        modReturn = [str(the_modifier.type), the_modifier.modval]
        totalModList.append(modReturn)

    for results in listOfDiceSets:
        diceSetResults = results
        dicePoolResultsLabel = Label(rollHistoryFrame, text=diceSetResults)
        dicePoolResultsLabel.pack(anchor=NW, side=TOP)

    for finalSetofMods in totalModList:
        finalModsetLables = Label(rollHistoryFrame, text=finalSetofMods)
        finalModsetLables.pack(anchor=NW, side=TOP)
       


def clickClearHistory ():
    def clear_rollHistoryFrame():
        for widgets in rollHistoryFrame.winfo_children():
            widgets.destroy()
    clear_rollHistoryFrame()
            


root = Tk()
root.title("Dice Roller")

#frame for dice pool entry
dieFrame = Frame(root)
dieFrame.grid(row=0, column=0, padx=10, pady=10)

dieEntryLable = Label(dieFrame, text="Name")
dieEntryLable.grid(row=0, column=0)

dieEntryField = Entry(dieFrame)
dieEntryField.grid(row=0,column=1)

dieSideLable = Label(dieFrame, text="Sides")
dieSideLable.grid(row=1, column=0)

dieSideEntry = Entry(dieFrame)
dieSideEntry.grid(row=1, column=1)

dieCountLable = Label(dieFrame, text="Count")
dieCountLable.grid(row=2, column=0)

dieCountEntry = Entry(dieFrame)
dieCountEntry.grid(row=2, column=1)

#add to pool button
addToPoolButton = Button(dieFrame, text="Add to Pool", width=20, command= lambda: poolManager("Add"))
addToPoolButton.grid(row=3, column=0, columnspan=2)



#frame for modifier entry
modFrame = Frame(root)
modFrame.grid(row=1, column=0, padx=10, pady=10)

modLabel = Label(modFrame, text="Name")
modLabel.grid(row=0, column=0)

modNameEntry = Entry(modFrame)
modNameEntry.grid(row=0, column=1)
modNameEntry.insert(0, "Modifier")

modValLabel = Label(modFrame, text="Value")
modValLabel.grid(row=1, column=0)

modValEntry = Entry(modFrame)
modValEntry.grid(row=1, column=1)

#button that adds modifiers to pool
addModButton = Button(modFrame, text="Add Modifier", width=20, command= lambda: modManager("Add"))
addModButton.grid(row=2, column=0, columnspan=2)


#frame for dice pool collection
poolFrame = Frame(root)
poolFrame.grid(row=0, column=1)

poolDataFrame = Frame(poolFrame, bg="black", width=350, height=100)
poolDataFrame.pack(side=TOP, padx=5, pady=5)

#the clear pool button
clearPoolButton = Button(poolFrame, text="Clear Pool", width=20, command= lambda: poolManager("Clear"))
clearPoolButton.pack(side=TOP, padx=5, pady=5)


#frame for modifier pool collection
modCollectFrame = Frame(root)
modCollectFrame.grid(row=1, column=1)

modDataFrame = Frame(modCollectFrame, bg="black", width=350, height=100)
modDataFrame.pack(padx=5, pady=5)

clearModButton = Button(modCollectFrame, text="Clear Modifiers", width=20, command= lambda: modManager("Clear"))
clearModButton.pack(side=TOP, padx=5, pady=5)

#big roll button to initiate roll of dice pool
theRollButton = Button(root, width=20, height=5, text="ROLL", command=clickRollButton)
theRollButton.grid(row=2, column=0, columnspan=2)

#frame for roll result and history
rollHistoryFrame = Frame(root, width=40, height=30)
rollHistoryFrame.grid(row=3, column=0, columnspan=2)

clearHistoryButton = Button(root, width=20, text="Clear History", command=clickClearHistory)
clearHistoryButton.grid(row=4, column=0, columnspan=2, pady=5)



root.mainloop()