try :   # Will Get weight from user  
    weight = float(input("Enter your weight "))
except ValueError: # Type this message if user enters a non-numeric value
    print("Please enter a valid number")
    exit()
convertor = input("Enter (L)bs or (K)g").lower()    # .lower() will convert the input to lower case so that the user can enter either upper or lower case letters
if convertor == "l":
    cweight = weight / 2.205 
    print(f"Your weight in KG(s) is {cweight}")
elif convertor == "k":
    cweight = weight * 2.205 
    print(f"Your weight in LB(s) is {cweight}")
