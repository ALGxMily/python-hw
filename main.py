import time

shoppingList = {}
choices = ("P","A","R","C","Q")

def menu():
    print("Press one of the following letters: ")
    print("P. Print List of the items to buy ")
    print("A. Add items to the list ")
    print("R. Remove Item from the list ")
    print("C. Change item from the list ")
    print("Q. Quit")
    return input("=> ").upper()
userChoice = menu()

def printList():
    if not shoppingList:
        print('Sorry looks like the list is empty')
        print("Redirecting you to the main screen... \n")
        time.sleep(1)
    else:
        print(f"You have {len(shoppingList)} items in your shopping list")
        for index,i in enumerate(shoppingList,1):
            print(f"{index}. {shoppingList[i]}")
        print("Redirecting you to the main screen... \n")
        time.sleep(1)

def addItems():
    countItems = int(input("How many items would you like to add? "))
    for i in range(countItems):
        items = input("Please add item: ")
        shoppingList[i] = items
    print(f"You have successfully added {countItems} to your shopping list!")
    print("Redirecting you to the main screen... \n")
    time.sleep(1)

def removeItems():
    print("Choose an item that you want to remove: ")
    for index,i in enumerate(shoppingList,1):
        print(f"{index}. {shoppingList[i]}")
    itemChosen = int(input("Enter choice => "))
    del shoppingList[itemChosen-1]
    print("Updated list: ")
    for index,i in enumerate(shoppingList,1):
        print(f"{index}. {shoppingList[i]}")
    time.sleep(2)
    print("Redirecting you to the main screen... \n")
    time.sleep(1)

def changeItems():
    print("Choose an item that you want to change: ")
    for index,i in enumerate(shoppingList,1):
        print(f"{index}. {shoppingList[i]}")
    itemChosen = int(input("Enter choice => "))
    updatedItem = input("Enter new value: ")
    shoppingList[itemChosen-1] = updatedItem
    print("Updated list: ")
    for index,i in enumerate(shoppingList,1):
        print(f"{index}. {shoppingList[i]}")
    time.sleep(2)
    print("Redirecting you to the main screen... \n")
    time.sleep(1)


while True:
    while userChoice not in choices:
        time.sleep(0.5)
        userChoice = menu()
    if userChoice == "P":
        printList()
        userChoice = ""
    elif userChoice == "A":
        addItems()
        userChoice = ""
    elif userChoice == "R":
        removeItems()
        userChoice = ""
    elif userChoice == "C":
        changeItems()
        userChoice = ""
    elif userChoice == "Q":
        print("\n")
        print("Thanks for using this application!\n".center(60))
        break