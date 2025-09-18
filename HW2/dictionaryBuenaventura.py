
size = int(input("Please enter number for matrix size: "))
myYellowBasket = {}



for index in range(size):
    basketItem = input(f"Shopping Item {index+1}: ")
    myYellowBasket[index] = basketItem

print(f"\nYou have {len(myYellowBasket)} items in the cart")





while True:
    action = input("\nWhat would you like to do [C]hange [R]emove [D]isplay [S]earch ? ")

    if action == "*":
        print("Bye!!")
        break

    elif action.lower() == "d":
        print("\nKey   Value")
        for basketKey, basketItem in myYellowBasket.items():
            print(f"{basketKey:<5} {basketItem}")

    elif action.lower() == "s":
        searchInput = input("\nEnter item or key to search: ")
        isFound = False

        for basketKey, basketItem in myYellowBasket.items():
            if searchInput == basketItem:  # match by value
                print(f"Found {basketItem} item at key {basketKey}")
                isFound = True
                break


            elif searchInput.isdigit() and int(searchInput) == basketKey:  # match by key
                print(f"Key {basketKey} contains {basketItem}")
                isFound = True
                break


        if not isFound:
            print(f"I'm sorry, {searchInput} not in the cart.")


    elif action.lower() == "r":
        removeInput = input("\nEnter key or item to remove: ")
        isDeleted = False

        for basketKey, basketItem in list(myYellowBasket.items()):

            if removeInput == basketItem:
                print(f"The key {basketKey} with value {basketItem} has been deleted.")
                myYellowBasket.pop(basketKey)
                isDeleted = True
                break


            elif removeInput.isdigit() and int(removeInput) == basketKey:
                print(f"The key {basketKey} with value {basketItem} has been deleted.")
                myYellowBasket.pop(basketKey)
                isDeleted = True
                break


        if not isDeleted:
            print(f"Key or item '{removeInput}' not found.")


    elif action.lower() == "c":
        changeInput = input("\nEnter key or item to change: ")
        isUpdated = False

        for basketKey, basketItem in myYellowBasket.items():
            if changeInput.isdigit() and int(changeInput) == basketKey:
                newValue = input(f"Enter new value for key {basketKey}: ")
                myYellowBasket[basketKey] = newValue
                isUpdated = True
                break
            elif changeInput == basketItem:
                newValue = input(f"Please enter new value for item {basketItem}: ")
                myYellowBasket[basketKey] = newValue
                isUpdated = True
                break
        if not isUpdated:
            print(f"{changeInput} - sorry, not found in cart.")

    else:
        print("Invalid. Error. Please try again.")
