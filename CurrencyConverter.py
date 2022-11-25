print("Welocme to currency converter!")
print("Please choose the option in which you want to convert your currency:")
print("Select 1: INR -> USD \n"
      "Select 2: INR -> EURO \n"
      "Select 3: INR -> CNY \n"
      "Select 4: INR -> GBP \n"
      "Select 5: INR -> AUD")
print("---------------------------------------------------------")
print("Please Enter the Option:")  

choice = int(input())
amount = 0
print("---------------------------------------------------------")
print("Selected option is:",choice)


if(choice == 1):
    print("Please enter the amount you want to convert:")
    amount = float(input())
    print("\n According to current conversion rates:")
    print("\n 1 USD = 81.51Rs")
    print("\n After Conversion:")
    print("-------------------------------------------")
    print("The amount is:",amount//81.5)
    print("\n")
elif(choice == 2):
    print("Please enter the amount you want to convert:")
    amount = float(input())
    print("\n According to current conversion rates:")
    print("\n 1 EURO = 84.99Rs")
    print("\n After Conversion:")
    print("-------------------------------------------")
    print("The amount is:",amount//84.99)
    print("\n")
elif(choice == 3):
    print("Please enter the amount you want to convert:")
    amount = float(input())
    print("\n According to current conversion rates:")
    print("\n 1 11.38 = 81.51Rs")
    print("\n After Conversion:")
    print("-------------------------------------------")
    print("The amount is:",amount//11.38)
    print("\n")
    print("Please enter the amount you want to convert:")
elif(choice == 4):
    print("Please enter the amount you want to convert:")
    amount = float(input())
    print("\n According to current conversion rates:")
    print("\n 1 GBP = 98.70Rs")
    print("\n After Conversion:")
    print("-------------------------------------------")
    print("The amount is:",amount//98.70)
    print("\n")
    print("Please enter the amount you want to convert:")
elif(choice == 5):
    print("Please enter the amount you want to convert:")
    amount = float(input())
    print("\n According to current conversion rates:")
    print("\n 1 AUD = 55.08Rs")
    print("\n After Conversion:")
    print("-------------------------------------------")
    print("The amount is:",amount//55.08)
    print("\n")
    print("Please enter the amount you want to convert:")
else:
    print("Wrong option selected!") 

