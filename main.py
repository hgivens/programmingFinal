
print("                   Welcome to the Car Shop")

def printUserMenu():
    print("\n=============================================================================================")
    print("1: Whats in your cart")
    print("2: Add a car to cart")
    print("3: Remove an item ")
    print("0:Check out ")

def listCartItems(menuItems):
    count = 0
    for menuItem in menuItems:
        count += 1
        print("--Item " +str(count) + ": " + menuItem + "--")

userChoice = None
menuItems = []

while userChoice != 0:
    printUserMenu()
    try:
        userChoice = int(input("Please enter a number: "))
    except:
        print("Please enter a valid number (0-3)")
        continue
    if userChoice == 0:
        file_write = open("cart.txt", "w")
        file_write.write("Are you ready to check out?\n")
        file_write.write("this is what you got:\n "+ menuItems)
        print("Good By, Come Again!")
        break
    elif userChoice == 1:
        listCartItems(menuItems)
    elif userChoice == 2:
        print(""" 
            Engines       |          Car Type 
      ================================================      
      -v6         $6,000  |    -Toyota    $15,000
      -4cylinder  $3,000  |    -Ford      $14,000  
        

        please enter the engin and or car type with price.
        """)
        item = input("Please enter an Item to add: ")
        while len(item) == 0:
            item = input("Nothing entered, try again: ")
        menuItems.append(item)
    elif userChoice == 3:
        print("Here are the current items in cart: ")
        listCartItems(menuItems)
        item = int(input("Please enter the item number you like to remove: "))
        menuItems.pop(item-1)
    else:
        print("Enter a Valid Number: ")
