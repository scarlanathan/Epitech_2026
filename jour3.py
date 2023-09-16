from operator import countOf
import itertools
import re



s = input('put string in variable')
print(s)

def character(s): #print 1er character et 5
    i = 0
    for a in s:
        i+=1
        if i == 1:
            print (a)
        elif i == 5:
            print (a)
    return None

def last(s): #print dernier character print(s[-1]) marche aussi
    i = 0
    for a in s:
        i+=1
        if i == len(s):
            print(a)


def character2(s): #print 5 à 10 
    i = 0
    b = ""
    for a in s:
        i+=1
        if 4<i | i<11:
            b = b+a
    return b

def minuscule():
    s = input('put in string variable \n ')
    return s.lower()

def change(): #remplace tu par ta
    m = input('put in string variable \n ')
    print(m.replace("tu","ta"))
    return None

#string methods task2 
# position = string.find("a") cherche l'itération où il y a la lettre' "a" dans string retourne -1 car il y en a pas


#string methods task3
#[::-2] - signifie qu'on commence par la fin 
#       le 2 signifie qu'on saute 2 par 2
#[:5]   on prend toute les valeurs jusqu'a 5 inclus
#[3:]   on prend les valeurs a partir de 3 exclu jusqu'à la fin

#string methods task4
#print(p[-2])

def tentime():
    s = input('put in string variable \n ')
    for i in range (10):
        print(s)
    return None

def tentime2(s):
    for i in range (10):
        print(s)
    return None

#string methods task7
# soit s2 = "42"
#soit concat ) s1 + str(s2)


#string methods task8
#concat = "\"%s %s %s\" contains 16 " %(string1,string2,string3)
#print (" The string %scharacters." % (concat)) 

def split_list(lst, val):
    return [list(group) for k,
            group in
            itertools.groupby(lst, lambda x: x==val) if not k]

def occurence():
    nb = 0
    a = " \s+"
    #strings = input('put in string variable \n ')
    #on peut aussi index qqn part
    strings = "thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN"
    strings = strings.lower()
    nb = strings.count("cat") + nb
    nb = strings.count("garden") + nb
    nb = strings.count("mice") + nb
    nb = strings.count("tac") + nb
    nb = strings.count("nedrag") + nb
    nb = strings.count("ecim") + nb
    return nb


def hello():
    a = input("What is your username?")
    return 'Hello ' + a

def hello2():
    a = input("What is your name?")
    return a[:1].upper()+ " " + hello()

def summ():
    a = int(input("put a number"))
    b = int(input("put second number"))
    return ("The sum of the two provided nuùmbers is sum %i"%(a+b))

def ask():
    a = int(input("give me any number"))
    return type(a)

def sentence():
    strings = "This is a test. Is it possible to fly? Good things cometo those who never give up"
    a = ""
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    taille = len(strings) - 5
    for i in range (taille):
        print(strings[0])
        if abc.find(strings[0]) != -1:
            for i in range(taille):
                if strings[i] != " ":
                    a = a + strings[i]
                else:
                    a = a + " "
                    strings= strings[1:]
                    break
            else:
                break
        strings= strings[1:]
    return a