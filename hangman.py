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
    