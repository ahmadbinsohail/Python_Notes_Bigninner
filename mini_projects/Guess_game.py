guess_num = int(7)  # Secret number to be guessed
admin_pass = "admin123"  # Admin password for changing game settings
option = int(0)
status = int(1)  # Game continues while this is 1

'''play = int(0)
while play != 1 and play != 0:
        play = int(input("""Press 1 to Play 
Press 0 to exit 
"""))'''  # Optional play menu kept as comments for reference
    
while status == 1:  # Main game loop
    
    i = 0
    guess_limit = int(0)
    while guess_limit < 3 :  # Player has only 3 attempts in this round
        while guess_num != i :
            i =int(input ("Guess Number "))
            guess_limit = guess_limit + 1
            if i != guess_num :
                print("Wrong Number ")
                print(f"{ 3 - guess_limit} tries left")
                break
            elif i == guess_num :
                print("""Correct 
                You Won""")
                break
        if i == guess_num :
            break
    if guess_num != i :  # If player did not guess correctly in time
        print("You lost")
    status = int(input("""Press 0 to exit
Press 1 to restart
Press 2 to change number 
"""))  # Ask the player for the next action
    if status != 0 and status != 1 and status != 2 :
        while status != 0 and status != 1 and status != 2 :
            status = int(input("""Invalid option
Press 0 to exit
Press 1 to restart
Press 2 to change number 
"""))  # Keep asking until the choice is valid
    
    if status == 0 :  # Exit the game
        
        print("Succefully Exit!")
        break
    elif status == 2 :  # Admin access to modify the game
        user_entered_password = input("Enter password to access admin's authorities ")
        while user_entered_password != admin_pass :
            user_entered_password = input("Wrong password , try again ")  # Re-prompt until password matches
        admin_options = int(0)
        admin_options = int(input("""Press 1 to change number
    Press 2 to change password
    """))  # Choose admin action
        while admin_options != 1 and admin_options != 2 :
            admin_options = int(input("""Invalid option
    Press 1 to change number
    Press 2 to change password 
    """))  # Validate admin menu choice
        if admin_options == 1 :  # Change the secret number
            guess_num = int(input("Enter the guess number "))
            print(f"Number changed Succesfully New number is {guess_num}")
            status = 1
        elif admin_options == 2 :  # Change the admin password
            admin_pass = input("Enter new password ")
            print("Password Updated ")
            status = 1