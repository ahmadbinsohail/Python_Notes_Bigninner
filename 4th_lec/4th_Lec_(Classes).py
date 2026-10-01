#Classes

class Human :
    def __init__(self,x,y,n):
        self.x = x
        self.y = y
        self.name = n
 
    age = 0
    height = 0
    color = 0
    def speak(self):
         print(f"Hi i'am {self.name}")

    def eat(self):
        print("Eating")

ahmad = Human(1,1,"Ahmad Raza")  # Create a Human object named ahmad with x=1, y=1, and name='Ahmad Raza'
print(ahmad.age)  # Print ahmad's age value (initially 0 from the class)
ahmad.speak()  # Call the speak() method to print: Hi i'am Ahmad Raza
ahmad.age = 20  # Change ahmad's age to 20
print(ahmad.age)  # Print the updated age value (20)
print(ahmad.x)  # Print ahmad's x coordinate value (1)
print(ahmad.y)  # Print ahmad's y coordinate value (1)
ali = Human(2,2,"Ali raza")  # Create another Human object named ali with x=2, y=2, and name='Ali raza'
print(ali.x)  # Print ali's x coordinate value (2)
print(ali.y)  # Print ali's y coordinate value (2)
print(ali.age)  # Print ali's age value (initially 0)
ali.eat()  # Call ali's eat() method, which prints 'Eating'
Human.eat(ahmad)  # Call the eat() method on ahmad explicitly using the class
print(ahmad.name)  # Print ahmad's stored name
print(f"Hi my name is {ahmad.name}")  # Print a formatted message using ahmad's name

# Inheretence 
class Men(Human):
    def __init__(self, n):
        super().__init__(0,0,  n)
        self.hair = "Short"


class Women(Human):
    def __init__(self,n):
        super().__init__(0,0,n)
        self.hair = "Long"


asma = Women("Asma")
asma.eat()
print(asma.hair)
tayyab = Men("Tayyab")
tayyab.speak()
print(tayyab.hair)
print(tayyab.age , asma.age,)