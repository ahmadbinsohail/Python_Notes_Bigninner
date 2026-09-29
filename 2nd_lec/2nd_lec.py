# arithmetic operators
#single division for getting original value
a , b = 5 , 6
print(a / b)

# double division to get the intiger force fully

print(a // b)

# exponension (use power after the ** and it will solve it on it's own)

print(a**b)

# augmented assingment operator
print(a)
a += 3
print(a)
OP = '''
# Operator prcedence 
1   ()
2   **    (exponention)
3   +b, -a  (uniary increment )
4    *,/ ,//,%
5     =,-
6     <<,>>
7     &
8     ^
9     |
10    == , <= , >=
11    not
12    and 
13    or
14    = , += ,-=                            
'''

# MATH FUNCTIONS   ( date : 9/5/2026)

# round function 
mf = -4.6
print(round(mf))

# absolute fucntion 

print(abs(mf))
mf = abs(mf)
# Modules (type . to use it)

import math 
print(math.ceil(mf))
print(math.floor(mf))
print(math.trunc(mf))
mf = int(mf)
print(mf)
print(math.fabs(mf))
print(math.factorial(mf))
print(math.isqrt(mf))
print(math.comb(10,mf))
print(math.perm(10,mf))
print(math.fmod(a,b))
mf = float(mf)
print(math.modf(mf))

# if (else , esls if ) statement 

stringdemo = "hot"
is_ture = True
is_false = False
if is_ture:
    print("It's true buddy ")
    print("Enjoy your coding session")
elif is_false:
    print("It's wrong also buddy ")
else:
    print("it nothing brother")

pofhouse = 100000 
cofb = True
if cofb:
     downp = 0.1 * pofhouse 
else :
      downp = 0.2 * pofhouse
downp = int(downp)
print(f"Your down payment is {downp} PKR ")

# logical & comparison operators        # while loop
name = input("Enter your name ")
while len(name) > 50 or len(name) < 3:
     
     if len(name) < 3 :
        print("Name must have minimume 3 characters")
        name = input("Enter your name ")
     elif len(name) > 50 :
        print("Name must under 50 chracters")
        name = input("Enter your name ")
else:
     print(f"Nice to meet you {name}")




