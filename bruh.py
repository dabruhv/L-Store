

inventory = [0,0,0]
money = 100
inStore = True

def store(fund):
    
    sus = input("(b)uy or (s)ell")
    if sus == 's':
        sus = input("are you sellin (r)ocks for 5 credits, (p)otions for 10 credits, or (d)arts for 12 credits?")
        if sus == 'r':
            amnt = int(input("how many rocks?"))
            if fund >= amnt:
                print("business")
                fund += 5*amnt
                inventory[0]-=amnt
                
            else:
                print("bruh")
                
        elif sus == 'p':
            amnt = int(input("how many potions?"))
            if fund >= amnt:
                print("business")
                fund += 10*amnt
                inventory[1]-=amnt
                
            else:
                print("bruh")
                
        elif sus == 'd':
            amnt = int(input("how many darts?"))
            if fund >= amnt:
                print("business")
                fund += 12*amnt
                inventory[2]-=amnt
                
            else:
                print("bruh")
                
    elif sus == 'b':
        sus = input("are you buyin (r)ocks for 5 credits, (p)otions for 10 credits, or (d)arts for 12 credits?")
        if sus == 'r':
            amnt = int(input("how many rocks?"))
            if fund >= amnt*5:
                print("business")
                fund -= 5*amnt
                inventory[0]+=amnt
                
            else:
                print("bruh")
                
        elif sus == 'p':
            amnt = int(input("how many potions?"))
            if fund >= amnt*10:
                print("business")
                fund -= 10*amnt
                inventory[1]+=amnt
                
            else:
                print("bruh")
                
        elif sus == 'd':
            amnt = int(input("how many darts?"))
            if fund >= amnt*12:
                print("business")
                fund -= 12*amnt
                inventory[2]+=amnt
                
                
            else:
                print("bruh")
    return fund



while inStore is True:
    print("you have ",money," credits")
    print("rocks: ",inventory[0], " potions: ", inventory[1], " darts: ", inventory[2])
    decide = input("do you want to leave the store?y/n")
    if decide == 'y':
        inStore = False
    else:
        money = store(money)


print("Thank You Come Again!")
        
