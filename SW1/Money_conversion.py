def Converter(pera):
    rupees = pera * 82.50
    pound = pera * 0.80
    yuan = pera * 7.30
    return rupees, pound, yuan

while True:
    pera = input("Enter dollar ($) (* to exit): ")
    if pera.strip() == "*":
        print("Bye")
        break

    splitter = pera.split("@")
    listOfPera = []

    for i in splitter:
        listOfPera.append(int(i))


    print(f"\n{'Dollar ($)':<12}{'Indian Rupee (R)':<18}{'British (Pound)':<20}{'China (Y)':<15}")
    

    for separatedPera in listOfPera:
        rupees, pound, yuan = Converter(separatedPera)
        print(f"{separatedPera:<12}{rupees:<18.2f}{pound:<20.2f}{yuan:<15.2f}")
    print()
