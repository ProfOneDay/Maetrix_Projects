

while(True):
    
    row = int(input("Enter row: "))
    column = int(input("Enter column: "))
    search = int(input("Enter search: "))

    if row <= 0 or column <= 0:
        print("Error! Must only put 1 above.")
        break

    for i in range(1, row + 1):
        for x in range(1, column + 1):
            if(search == i*x):
                print(f"[{i*x}]", end = " ")
            else:
                print(i * x, end = " ")

        print()