class Dice:      #Dice class used so more than one dice can b used
    def dice_number() :
        import random     #Used to get random values for dice
        status = True
        while status :
            try:
                n_d = int(input("Select number of dice\s "))
                status = False
            except ValueError:
                print("Invalid entry")
        return n_d
    def roll(n_d):   #roll funtion to get random values
        import random
        staus = True
        while staus:
            s_d = input("Press R to roll the dice").lower()
            if s_d == "r":
                for i in range(n_d):
                    print(random.randint(1,6),end=" ")
                staus = False
            else:
                print("Invalid entry")
d1 = Dice
n = d1.dice_number()
d1.roll(n)