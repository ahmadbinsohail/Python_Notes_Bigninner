# Auto iteration 
for x in range(10):
    print(f"Hi {x}")

for x in range(3,6):
    print(x)

# range( start , end , increment/jump)
for x in range(2, 20 , 5):
    print(x)

# Exercise Totall cost of shopping cart
shopping_cart = [100,200,1990,45]
totall = 0
for x in shopping_cart:
    #totall = totall + x
    totall += x
print(totall)

# Nested loops
#exersice to draw F
list_f = [5,2,5,2,2]
#for f in list_f:
 #   print(f*"x")
# in nested method
for r in list_f :
    srt = " "
    for f in range(r) :
        srt += "X"
    print(srt)

# Listis
names = ["Ahmad",  "Abdullah", "Qasim" , "Aqib" , "Subhan" , "Danish" , "manymore"]
print(names)
#Exercise find largest 
numbers = [1,54,35,76,-1,-25,-100,43,36,35,75,24,35,67]
g = 0
count = 0
for x in numbers:
    if x > g :
        g = x
    count += 1
    print(count)
print(f"Greatest Number in {numbers} is {g}")

# 2D lists , lists within a list 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[1][2])
for r in matrix:
    for e in r:
        print(e)

# Methods in lists
numbers.append(100) #add to last
print(numbers)
numbers.insert(0,10) # add to specific place
print(numbers)
numbers.extend([101,102,103]) # an other iterable like list or tuple
print(numbers)
numbers.pop(-1) #return and remove number 
print(numbers)
numbers.remove(100) # find and remove a specific value #Raises error
print(numbers)
numbers2 = numbers.copy()
print(numbers)
print(numbers2)
 # remove all the elements form the lists
numbers2.clear()
print(numbers2)
numbers.index(54) #returns index , raises error
print(numbers)
print(numbers.count(35)) # counts totall specific values 
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

# Exercise 

numbers =  [1, 4, 66, 66, 43, 4, 66, 70, 4, 1, 100, 70, 4,1,1,1,1,1,1,4,4,4,4]
loop_num = numbers.copy()
print(numbers)
for c in loop_num :
    compare = 0
    compare = numbers.count(c)
    if compare > 1 :
        numbers.remove(c)
numbers.sort()
print(numbers)

# TUPELS # can't modifiy
cordinates = (1,2,3,4)
x,y,z,b= cordinates
print(x,y,z,b)

# Dictionries
manager = { 
    "name" : "Mr.Manager",
    "age" : 20,
    "salary" : 200000,
    "verified" : True
}
print(manager.get("name"))
print(manager.get("Name","Not Found Your value"))
print(manager.get("age", "Not found your data"))
# print(manager["Age", "Not found your data"]) , this will not work 

# Exercise 

numbers = {
    "0" : "Zero",
    "1" : "ONE",
    "2" : "TWO",
    "3" : "THREE",
    "4" : "FOUR",
    "5" : "FIVE",
    "6" : "SIX",
    "7" : "SEVEN",
    "8" : "EIGHT",
    "9" : "NINE"
}
cell = input("Phone : ")
for c in cell:
    print(numbers.get(c,"?"),end=" ")
print(" ")

# Funtions    #obligated to save value in parameters 
first_name = input ("Enter your first name : ").title()
last_name = input ("Enter your last name : ").title()
def salam(fn,ln):    #parameters
    print(f"Aslamualikum {fn} {ln} Bhai")
    print("Umeed ha khareet sy hogy")


print("Or bhai ")
salam(first_name , last_name )   #arguments (positional arguments)
print("Chalo phir milty han")
salam( last_name , first_name)           #arguments (positional arguments)
salam( fn=last_name , ln=first_name )     #arguments (Keyword arguments)


# Return Statements

def square(x ):
    return x*x
a = int(input("Enter a numeric digit "))
print(f"Square of {a} is ",square(a))

# Emoji convertor funtion 

def emoji_convertor(m):
    emoji = {
            "sad" : "😔",
            "happy" : "😊",
            "funny" : "😂",
            "smile" : "😊",
            "love" : "😘",
            "angry" : "😡",
            "rude" : "😒"
        }
    words = m.split()
    output_emoji = " "
    for word in words:
        #print(emoji.get(word,word))
        output_emoji += emoji.get(word,word) + " "
    return output_emoji


message = input("Enter your Message ")
output = emoji_convertor(message)
print(output)