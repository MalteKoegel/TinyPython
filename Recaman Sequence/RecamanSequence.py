from tkinter import *


window = Tk()
selection = IntVar()
text = StringVar()
stringValue = StringVar()



def sequenceCounter(limit):

    currentSequence_list = [0]
    currentStepSize = 1

    def oneStep(value, currentStepSize, currentSequence_list):
        if not currentSequence_list.__contains__(value - currentStepSize) and (value - currentStepSize)>=0:
            value = value - currentStepSize
        else:
            value = value + currentStepSize
        return value

    if (selection.get() == 0):
        print("\n")
        limit -= 1
        for i in range(0,limit):
            currentSequence_list.append(oneStep(currentSequence_list[len(currentSequence_list)-1], currentStepSize, currentSequence_list))
            currentStepSize += 1
    elif(selection.get() == 1):
        print("\nMaximum Number: " + str(limit))
        while currentSequence_list[len(currentSequence_list)-1]<=limit:
            currentSequence_list.append(oneStep(currentSequence_list[len(currentSequence_list)-1], currentStepSize, currentSequence_list))
            currentStepSize += 1
        if currentSequence_list[len(currentSequence_list)-1]>=limit:
            currentSequence_list.pop(len(currentSequence_list)-1)
    elif (selection.get() == 2):
        print("\nTarget Number: " + str(limit))
        while currentSequence_list[len(currentSequence_list) - 1] != limit:
            currentSequence_list.append(
                oneStep(currentSequence_list[len(currentSequence_list) - 1], currentStepSize, currentSequence_list))
            currentStepSize += 1
    print ("Number of Steps: " + str(len(currentSequence_list)))
    print("Recamán's Sequence: " + str(currentSequence_list).replace("[", "").replace("]", ""))


def createWindow():
    def updateEntry():
        if (selection.get() == 0):
            text.set("Enter number of steps:")
        elif (selection.get() == 1):
            text.set("Enter maximum number:")
        elif (selection.get() == 2):
            text.set("Enter target number:")


    # set up window
    window.wm_title("Recamán's Sequence")
    window.minsize(width = 300, height = 150)

    # set up radio buttons
    RB_numberOfSteps = Radiobutton (window, text="Number of Steps", variable = selection, value = 0, command = updateEntry)
    RB_maxNumber = Radiobutton (window, text ="All numbers smaller than or equal to", variable = selection, value = 1, command = updateEntry)
    RB_targetNumber = Radiobutton(window, text ="Until this number is reached", variable = selection, value = 2, command = updateEntry)
    #set up entry
    label_textField = Label(window, textvariable = text, font = "Helvetica 12 bold")
    textField = Entry(window, textvariable = stringValue, justify = RIGHT)
    #set up button
    startButton = Button(window, text="Start", command = lambda:sequenceCounter(int(stringValue.get())))

    label_textField.pack(side = TOP, anchor = W)
    textField.pack(anchor = W)
    RB_numberOfSteps.pack(anchor=W)
    RB_maxNumber.pack(anchor=W)
    RB_targetNumber.pack(anchor=W)
    startButton.pack(side = BOTTOM, anchor = E)
    updateEntry()
    window.mainloop()

createWindow()
