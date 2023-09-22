from random import randrange

def occurence(list,letter):
    res = ""
    for i in range(len(list)):
        if list[i] == letter:
            return True
    return False


def show(list,blank,letter):
    c = [i for i in blank]
    a = [i for i in list]
    nbr = 0
    for i in range (len(a)):
        if a[i] == letter:
            c[i] = letter
            nbr += 1
    print ("Found %i '%s'"%(nbr,letter))
    #b = " ".join(c)
    #print (b)
    return c

def hangman():

    guess = ""
    blank = ""
    affichage = ""
    tmp = ""
    tmp2 = ""
    points = 0
    list=["jeu","cordial","moche","koala","momie","rigolade"]
    word = list[randrange(4)]
    word = word.upper()

    for i in word :
        blank = blank + "_"
        affichage = affichage + " _ "
    print(affichage + " / O point")

    while guess != word:
        guess = input("guess a word or a letter\n")
        guess = guess.upper()
        if len(guess) == 1:
            if occurence(word,guess) == True:
                blank = show(word,blank,guess)
                tmp = "".join(blank)
                tmp2 =" ".join(blank)
                if points == 1 :
                    print (tmp2 + " / %i point"%points)
                else:
                    print (tmp2 + " / %i points"%points)
                if tmp == word:
                    print("%s: correct guess\nCongratulations !"%word)
                    print("%i points"%points)
                    return None
            else:
                print("No '%s' found"%guess)
                points += 1
                if points == 1:
                    print (affichage + " / %i point"%points)
                elif tmp2 == "":
                    print (affichage + " / %i points"%points)
                else:
                    print (tmp2 + " / %i points"%points)

        elif guess == word:
            print("%s: correct guess\nCongratulations !"%word)
            print("%i points"%points)
        else:
            points += 1
            print("%s: incorrect guess"%guess)
            if points == 1:
                print (affichage + " / %i point"%points)
            elif tmp2 == "":
                print (affichage + " / %i points"%points)
            else:
                print (tmp2 + " / %i points"%points)
    return None
    

def seven(a = "79712312"):
    for i in range(len(a)-1):
        if a[i] == "9":
            if a[i-1] == "7" and a[i+1] == "7":
                a = a.replace("9", "",1)
                i-=1
                if i > len(a)-1:
                    return a
    return a
    
def flush(a=["AS", "3S", "9S", "KS", "4S"]):
    b = []
    for i in a:
        i = i.replace("A","")
        i = i.replace("1","")
        i = i.replace("2","")
        i = i.replace("3","")
        i = i.replace("4","")
        i = i.replace("5","")
        i = i.replace("6","")
        i = i.replace("7","")
        i = i.replace("8","")
        i = i.replace("9","")
        i = i.replace("10","")
        i = i.replace("J","")
        i = i.replace("Q","")
        i = i.replace("K","")
        #print(i)
        b.append(i)
    print(b)
    s = 0
    h = 0
    d = 0
    c = 0
    for i in b:
        if i == "S":
            s +=1 
            if s == 5:
                return True
        elif i == "H":
            h +=1 
            if h == 5:
                return True
        elif i == "D":
            d +=1 
            if d == 5:
                return True
        elif i == "C":
            c +=1 
            if c == 5:
                return True
    return False

def projectPartenaire(n):
    return (n**2 - n )//2

def unique(list):
    sum =0
    a = 0
    while list != [] :
        sum += list[0]
        print(list[0])
        list.remove(list[0])
        print(list)

    return sum

unique([1,3,8,1,8])