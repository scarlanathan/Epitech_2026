#42>12
#12 =12
#12 ==12
#"hello" == "world"
#218 >= 118 
#"a".upper() == "A"
#1*2*3*4 <= 9
#"z" in "azerty"

def condi1():
    a = int(input("put integer "))
    if a == 42:
        print("Correcr answer")
    else : 
        print("Reprends ta vie en main")
    return None

def condi2():
    a = int(input("put integer "))
    if a%2 == 0:
        print("THis inter is even")
    else : 
        print("This integer is odd")
    return None

def condi3():
    a = input("give me the password\n")
    if a == "open sesame":
        print("access granted")
    elif a == ("will you open, you goddamn shit"):
        print ("access fucking granted")
    else:
        print ("permission denied")
    return None

def condi4():
    a = int(input("put integer\n"))
    if a == 42 or a <= 21 or a%2 == 0 or a/2 <= 21 :
        print("OK1")
    elif a%2 != 0 and a >= 45:
        print("OK")
    else:
        print("You got wrong my poor friend")
    return None

def condi5():
    a = 42
    b = 41
    if a == b:
        print ("A and B are the same")
    elif b <= a:
        print ("B is equal or lower than A")
    elif b != a:
        print("B is different from A")
    return None

def lop0():
    i = 0
    while i < 1000: 
        print (i+1)
        i+=1
    return None 

def lop1():
    a = input("put a string\n")
    b = ""
    for i in a:
        b = b + i + i
    return b

def lop2():
    i = 10000
    while i >= 1: #for i in range(1000,1,-1):
        if i%7 == 0:
            print (i)
        i-=1

def lop3():
    i = -30
    while i <=30:
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print ("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
        i+=1
    return None

def lop4():
    i = 99
    while i >=1 :
        if i == 1:
            print ("1 bottle of age-appropriate beverage on the wall 1 bottle of age-appropriate beverage on the wall")
            print ("nananananananana nanananananana")
        else:
            print ("%i bottles of age-appropriate beverage on the wall %i bottles of age-appropriate beverage on the wall Take one down, pass it around"%(i,i))
        i-=1
    return None

def lop5():
    n = int(input("put integer \n"))
    a = 2
    b = a
    display =""
    arret = n//2 - 1
    for i in range(arret): # 1 à n/2
        display = ""
        #print (n//2)
        #print(i)
        display = display + str(b)+" "

        while b < n: 
            b = b + a
            if b < n:
                display = str(b) + " " +display
        a+=1
        b = a
        print(display)
    return None


def challenge():
    voyelle = "aeiouyAEIOUY"
    a = int(input("gimme integer"))
    b = input("gimme sentence")
    for i in b:
        if voyelle.find(i) != -1 or a >= 42:
            print(a)
            break
        break
    if a == 0 :
        return None
    else :
        return b
    return None



def pi_challenge():

    x = input("Veuillez saisir un string: \n")
    y = int(input("Veuillez saisir un integer: \n"))

    exit() if y == 0 else print(y) if y >= 42 else print(y) if len([char for char in x if char in "aeiouyAEIOUY"]) >= 1 else print(x)

def cypher():
    a = int(input("number between 1 and 25\n"))
    b = input("message secret\n")
    reponse = ""

    for i in range(len(b)):
        char = b[i]
        
        if char == " ":
            reponse += " "
        elif char.isupper():
            reponse += chr((ord(char) + a - 65) % 26 + 65)
        else:
            reponse += chr((ord(char) + a - 97) % 26 + 97)
    return reponse
    
def decypher():
    a = int(input("number between 1 and 25\n"))
    b = input("message secret\n") 
    reponse = ""

    for i in range(len(b)):
        char = b[i]
        
        if char == " ":
            reponse += " "
        elif char.isupper():
            reponse += chr((ord(char) - a - 65) % 26 + 65)
        else:
            reponse += chr((ord(char) - a - 97) % 26 + 97)
    return reponse

def vigenere(decode):
    a = input("cle\n")
    b = input("message secret\n")
    reponse = ""

    for i,c in  enumerate(b):
        if c == " ":
            reponse += " "
        char = a[i % len(a)]
        char = ord(char) - 65
        if decode : char = 26 - char
        else:
            reponse += chr((ord(c)-65 + char) % 26 + 65)
    return reponse



def code_vigenere ( message, cle, decode = False) :
    message_code = ""
    for i,c in enumerate(message) :
        d = cle[ i % len(cle) ]
        d = ord(d) - 65
        if decode : d = 26 - d
        message_code += chr((ord(c)-65+d)%26+65)
    return message_code

def DecodeVigenere(message, cle):
    return code_vigenere(message, cle, True)
