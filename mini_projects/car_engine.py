def engine():
    # Setting default values
    command = "null"
    started = False 
    stopped = False
    help = """Enter any following command to run
        Start - Start the engine 
        Stop - Stop the engine
        Exit - Exit the Program """
    print(help)             #Message run to get the input
    while command != "exit" :     # while loop is used so that it will ask the input as many times as user wants
        command = input(">").lower()     # Used .lower() for input so user input case dosent affect the code working
        while command != "start" and command != "stop" and command != "exit" :   #if user enter's the odd input
            command = input(f"""I can't understand what are you saying 
            {help}""").lower()
        
        if command == "start":
            if started:
                print("Car is already started")   
            else :
                started = True
                print("Engine is started")
        elif command == "stop":
            if stopped :
                print("Engine is stopped")
            else :
                stopped = True
                print("car is already stupped")
    if command == "exit":
        print("Exit Succesfully ")
engine()
        