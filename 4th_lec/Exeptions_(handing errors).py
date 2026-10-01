try:  
    age = int(input("Enter your code here "))
    dev = 100 / age
    print(age)
except ValueError:
    print("Invalid Value ")
except ZeroDivisionError:
    print("Age cannot be zero ") 
    