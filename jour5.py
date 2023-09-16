def li1():
    liste = []
    for i in range (5):
        a = (input("put something in here\n"))
        liste.append(a)
    return liste

# print (liste(len(liste)-1))
def li2(nbre):
    liste = []
    for i in range (nbre):
        a = (input("put something in here\n"))
        liste.append(a)
    return liste[len(liste)-1]

def li3(liste):
    add = input("add somethinf on the list")
    liste.append(add)
    return liste
def li3bis():
    add = input("add somethinf on the list")
    liste = li1()
    liste.append(add)
    return liste

def li4(liste):
    for i in range(len(liste)-1):
        print(liste[i])
    return liste

def li5(liste):
    del(liste[-1])
    return  liste

def li6(liste):
    a = input("put something in here \n")
    liste.insert(0,a)
    return liste

def li7(liste):
    for i in range (1,5,1): # de 1 à 5 exclu 
        print(liste[i])
    return None

def li7bis(liste):
    return liste[1:5:1]

def li8(liste):
    liste2 = []
    for i in range(len(liste)-1,-1,-1):
        liste2.append(liste[i])
    return liste2

def li8bis(liste):
    liste2 = []
    for i in liste[::-1]:
        liste2.append(i)
    return liste2

def li9(liste):
    for i in liste[::2]:
        print(i)
    return liste[::2]

def li10(liste):
    for i in range(17):
        a = input("add element number %i\n"%i)
        liste.append(a)
    return liste
    
# first = [4,5,6]
# second = [1,2,3]
# first.extend(second)
# [4,5,6,1,2,3]

# first=[7,8,9]
# second= [4,5,6]
# first = [*first,*second] 
# print (first) 
#[7, 8, 9, 4, 5, 6]
from random import randrange

def op1():
    liste = []
    a = 1
    for i in range (10):
        liste.append(randrange(10))
        a = liste[i] * a
    return a

def op2(): # ajoute 10 à a la liste
    print([x+10 for x in [3,2,6,7,1,4]])
    return None

def op3():  #multipli au carré les valeurs de la liste
    print (list(map(lambda x : x*x,[3,2,6,7,1,4]))) #map permet de rentrer dans la liste et renvoie la valeur
    print([x**2 for x in [3,2,6,7,1,4]]) #lambda est une fonction
    return None

def op4():
    liste = [3,1,5,7,8,9]
    a = liste[0]
    b = liste[0]
    for i in liste:
        if i < b:
            b = i
        elif i > a:
            a= i
    print("biggest element is %i and the smallest is %i"%(a,b))
    return None
    
def op5(liste):
    for i in liste:
        if i < 7:
            print (i)
    return None

def op6(liste):
    liste.sort(reverse = True)
    print (liste)
    return None

def op7():
    print([x // 2 if x%2 == 0 else x*2 for x in [42,3,4,18,3,10]]) 
    return None

def op8():
    print(list(filter(lambda x :x > 10,[42,3,4,18,3,10]))) #filtre les nombres supérieurs a 10
    return None

def op9():
    print([*enumerate([42,3,4,18,3,10])]) #associe le nombre avec son index
    return None

def op10():
    first = ["Jaclie","Bruce","Arnold","Sylvester"]
    last = ["Stallons","Schwarzenegger","Willis","Chan"]

    magic = [*zip(first,last[::-1])]
    print(magic[0])
    print(magic[3])
    print(magic[1][0])
    print(magic[0][1])
    print(magic[2])
    return magic

import time
def challenge():
    startingTime = time.time()
    li = []
    for i in range (1000000):
        li.append(randrange(10))
    li.sort()
    duration = time.time()- startingTime
    #print (li)
    return duration

def dico1():
    a = input("put your name\n")
    b = input("academic year\n")
    student = {"name":a,"academic year":b}
    return student

def dico1bis(nbredestudent):
    listestud = ()
    for i in range (nbredestudent):
        listestud.append(dico1())
    return listestud

def dico2(student):
    units = {}

    a = randrange(5)+1
    if a == 1:
        grade = "A"
    if a == 2:
        grade = "B"
    if a == 3:
        grade = "C"
    if a == 4:
        grade = "D"
    if a == 5:
        grade = "E"
    
    b = input("enter W for Web Development or NS for Network and System Administration or JAVA\n")
    if b == "W":
        name = "Web Development"
        credits = 4
    if b == "NS":
        name = "Network and System Administration"
        credits = 5
    if b == "JAVA":
        name = "JAVA"
        credits = 3
    units =  {"Subject" : name , "credits":credits, "grade" : grade}
    student.update(units)
    return student

def dico3(student):
    grade_weight_mapping = {"A": 4, "B" : 3, "C" : 2, "D" : 1, "E" : 0}
    b = grade_weight_mapping.get(student.get("grade"))
    tcredits = student.get("credits") * b
    #t = {"total_credits": tcredits}
    student["total_credits"] = tcredits
    #student.update(t)
    highscore = 4 * student.get("credits")
    gpa = round(tcredits * 4 / highscore)
    g = {"gpa" : gpa}
    student.update(g)
    return student

def dico4():
    Tab = []
    a = {}
    for i in range (3):
        a = dico1()
        dico2(a)
        dico3(a)
        Tab.append(a)
    print(sorted(Tab, key =lambda d : d["name"]))
    print(sorted(Tab, key =lambda d : d["gpa"]))
    print(sorted(Tab, key =lambda d : d["gpa"],reverse=True))
    return None

def fur1():
    liste = ()
    a = input("name")
    for i in liste:
        if a == i:
            print ("welcome in")
        else :
            print("get lost")
    return None

def fur2():
    liste = ()
    for i in liste:
        for a in range(len(liste)):
            if i == liste[a] :
                liste.remove(a)
    return liste

def fur3(name):
    meeting = ["Monday", "3:30 PM", "Joe", "Samantha"]
    meeting1 = ["Monday", "3:30 PM", "Joe", "Samantha"]
    meeting2 = ["Monday", "3:30 PM", "Joe", "Samantha"]
    meeting3 = ["Monday", "3:30 PM", "Joe", "Samantha"]

    lst_meeting = [meeting,meeting1,meeting2,meeting3]

    for i in lst_meeting:
        for a in i:
            if a == name:
                print(i)
    return None




        
            
    






    



