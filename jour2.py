def task(n):
     i=0
     r=0
     for i in range (n):
             r = 10**i + r
             print (r)
     return r


def taskk(nombrede1,puissance):
     i=0
     temp=0
     resultat=0
     for i in range (nombrede1):
             temp = 10**i + temp
             resultat = temp + resultat
             print (resultat)
     return resultat**puissance

def task2():
       return 17**1024

def modulo():
       print(42/4)
       print (42//4)
       print (42%4)
       return None

def oddeven(n):
        if n%2 == 0:
               print("even")
        else:
               print("odd")
        return None

def sum(n):
       res = 0
       tab = [int(a) for a in str(n)]
       
       for i in tab:
              res = i + res
              print (res)
       return None

def rond(n):
        return int(n)

def task5(n):
       float (n)
       a = rond(n)
       return round(n-rond(a), 4)

def Pi(x):
    i=1
    p=0
    tmp=0
    for p in range (x):
            if p%2 == 0:
                tmp = tmp + 1/i
                i= i+2
            else:
                tmp = tmp - 1/i
                i = i+2
    res = 4*tmp
    return round(res,6)

    

def pii(x,p):
    b = p+2
    a = x
    tmp = 6
    if a !=  0 :
        a = a-1
        tmp = tmp + (b**2)/pii(a,b)
    return tmp

def pii2(x,p):
    return 3+1/pii(x,p)
    

def reduce(a,b):
    x = a
    y = b
    print("bonjour")
    if a%b == 0:
        x = a//b
        y = 1
    elif a%3 == 0 and b%3 == 0:
        while x%3 == 0 and y%3 == 0:
              x = x//3
              y = y//3
        reduce(x,y)
    elif a%5 == 0 and b%5 == 0:
        while x%5 == 0 and y%5 == 0:
              x = x//5
              y = y//5
        reduce(x,y)
    elif a%7 == 0 and b%7 == 0:
        while x%7 == 0 and y%7 == 0:
              x = x//7
              y = y//7
        reduce(x,y)
    elif a%11 == 0 and b%11 == 0:
        while x%11 == 0 and y%11 == 0:
              x = x//11
              y = y//11
        reduce(x,y)
    elif a%13 == 0 and b%13 == 0:
        while x%13 == 0 and y%13 == 0:
              x = x//13
              y = y//13
        reduce(x,y)
    elif a%17 == 0 and b%17 == 0:
        while x%17 == 0 and y%17 == 0:
              x = x//17
              y = y//17
        reduce(x,y)
    elif a%19 == 0 and b%19 == 0:
        while x%19 == 0 and y%19 == 0:
              x = x//19
              y = y//19
        reduce(x,y)
    elif a%23 == 0 and b%23 == 0:
        while x%23 == 0 and y%23 == 0:
              x = x//23
              y = y//23
        reduce(x,y)
    elif a%29 == 0 and b%29 == 0:
        while x%29 == 0 and y%29 == 0:
              x = x//29
              y = y//29
        reduce(x,y)
    elif a%31 == 0 and b%31 == 0:
        while x%31 == 0 and y%31 == 0:
              x = x//31
              y = y//31
        reduce(x,y)
    elif a%37 == 0 and b%37 == 0:
        while x%37 == 0 and y%37 == 0:
              x = x//37
              y = y//37
        reduce(x,y)
    elif a%41 == 0 and b%41 == 0:
        while x%41 == 0 and y%41 == 0:
              x = x//41
              y = y//41
        reduce(x,y)
    elif a%43 == 0 and b%43 == 0:
        while x%43 == 0 and y%43 == 0:
              x = x//43
              y = y//43
        reduce(x,y)
    elif a%47 == 0 and b%47 == 0:
        while x%47 == 0 and y%47 == 0:
              x = x//47
              y = y//47
        reduce(x,y)

    if a%2 == 0 and b%2 == 0:
        while x%2 == 0 and y%2 == 0:
            x = x//2
            y = y//2
        reduce(x,y)
        
    return (x,y)
            