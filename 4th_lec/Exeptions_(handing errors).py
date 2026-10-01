try:  
    age = int(input("Enter your code here "))
    dev = 100 / age
    print(age)
except ValueError:    #except is used to print value like invalid value in case of specific error occures
    print("Invalid Value ")
except ZeroDivisionError:     # You can use more than one except following a single try block 
    print("Age cannot be zero ") 
    