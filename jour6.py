def f(x):
    return 2 * x +1

def g():
    return 7

def bread():
    print ("</////////////////>")
    return None

def lettuce():
    print ("~~~~~~~~~~~~~~~~~~~")
    return None

def tomato():
    print ("0 0 0 0 0 0 0 0 0 0")
    return None

def ham():
    print("===================")
    return None

# bread(),lettuce(),tomato(),ham(),ham(),bread()


def sandwiches(nbre):
    if nbre < 0:
        print("I can't do this")
    else:
        for i in range (nbre):
            print(bread(),lettuce(),tomato(),ham(),ham(),bread())
            print()
    return None

def sandwiches2(nbre,spe = "ham"):
    if nbre < 0:
        print("I can't do this")
    elif spe == "vege":
        for i in range (nbre):
            print(bread(),lettuce(),lettuce(),tomato(),tomato(),bread())
    else:
        for i in range (nbre):
            print(bread(),lettuce(),tomato(),ham(),ham(),bread())
            print()
    return None

import time

def challenge():
    stratingTime = time.time()
    a = 42
    #print(42**84)
    for i in range (1,168,1):
        a = a * 42
    print (a)
    duration = time.time() - stratingTime
    return duration

# 0.015484333038330078 second for 168
# 0.0009984970092773438 second for 84

def lis(string):
    a = string.replace(".","")
    a = a.replace("?","")
    a = a.lower()
    a = a.replace(" ", "")
    #li = list(a.split(" "))
    return a

def palindrome(string, i = 0):
    string = lis(string)
    if i < len(string)//2:
        a = -i-1
        if string[i] == string[a]:
            i = i+1
            palindrome(string,i)
        else :
            print("ce n'est pas un palindrome")
            return None
    else : 
        print("c un palindrome")
    return None

import os
from os import walk

def d(p, s, j):
    root = '/home/nathan/epitech/pre/code_pre/Epitech_2026/test'
    path = "."
    print (os.listdir(root))
    for path, subdirs, files in range (len(os.walk(root))):
        print(os.path.join(path))
        #print(os.path.join(subdirs))
        for name in files:
            print(os.path.join(name), end="  ")
        print()


def lower(s,n):
    a = 0
    for i in s: 
        if i == i.lower():
            a+=1
    return a >= n

def upper(s,n):
    a = 0
    for i in s: 
        if i == i.upper():
            a+=1
            print(i)

    return a >= n

def character(s,n):
    return len(s) >= n

def special(s,n):
    a = 0
    for i in s:
        if i == "?" or i == "." or i == ":" or i == "!" or i == ";" or i == "," or i == "/":
            a += 1
    return a == n

def numbers(s,n):
    a = 0
    for i in s :
        if i == "0" or i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
            a += 1
    return a >= n

def check(a, b = 1 , c ="mysecretpassword//"):
    return a(c,b)

def check2(a, b = 1, c ="mysecretpassword"):
    if b <= 0:
        print("You don't search anything try again")
        return None
    if len(c) < 4:
        print("Password too short try again")
        return None
    if a == character or a == special or a == numbers or a == upper or a == lower:
        return a(c,b)
    else :
        print ("Wrong function try again")
        return None

def trianglee(t = "RRGBRGBB"):
    a = ""
    b = 0
    triangle = t
    if len(triangle) == 1:
        return triangle
    if b < len(triangle):
        for i in range(len(triangle)-1):
            if triangle[i] == "G" and triangle[i+1] == "G":
                a = a + "G"
            elif triangle[i] == "B" and triangle[i+1] == "B":
                a = a + "B"
            elif triangle[i] == "R" and triangle[i+1] == "R":
                a = a + "R"
            elif triangle[i] == "B" and triangle[i+1] == "G":
                a = a + "R"
            elif triangle[i] == "G" and triangle[i+1] == "B":
                a = a + "R"
            elif triangle[i] == "R" and triangle[i+1] == "G":
                a = a + "B" 
            elif triangle[i] == "G" and triangle[i+1] == "R":
                a = a + "B" 
            elif triangle[i] == "B" and triangle[i+1] == "R":
                a = a + "G" 
            elif triangle[i] == "R" and triangle[i+1] == "B":
                a = a + "G"
            else : 
                return t
        b += 1
        print(a)
        triangle = a
        triangle = trianglee(triangle)
    return triangle
    
        

