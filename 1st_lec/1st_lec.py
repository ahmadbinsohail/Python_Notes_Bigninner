# print statement 
print("Ahmad " * 5)

print("Welcome")
name = input("what is your name ").title()
print(f"Hi {name} Hope you doing well")
age = input("Enter your age ")

#Concadination

fvrtcolor = input("Enter your fovorutie colour ").upper()

#best way for doing it 

#print(f"{name} your favourte color is {fvrtcolor}")

print(name + ' your favourte color is '+ fvrtcolor)

#type coversion    #type 

#int(string) = intiger

winp = input(f"{name} what is your wieght      Note: IN POUNDS ")
wikg = int(winp) /  2.20462 
print(f"{name} your wieght in kilograms is {wikg}")
print(type(winp))

# if you want to qoutes for string 
# '
print(f'Hi "{name}" now you can see it')
# if you wanna use " then use ' outside
print(f"Now you can see' it ")
# multi line string '''
print(f''' Hi {name},
        Hope you are doing well
        regards programmer''')

# Indexes of the string in py

demostring = input("Enter a string ")
#for whole 
print(demostring[:])
#for a range   #3 is excluded
print(demostring[0:3])
#Starting from 4
print(demostring[4:-1])
#by default values
print(demostring[0:])
print(demostring[:-1])
print("All numbers at the end in range are excluded but from the the start part ")

#methods of strings
#len() for lenght  it's function      #methods have .in start     #it's case sensitive 
print(len(demostring))
findstring = f'Hello {name}'.lower()
print("ahmad" in findstring)
print("name" in findstring)