a = None
while a == None:
    try:
        a = float(input("a (legyen float) = "))
    except:
        print("Ez nem float!")
        a = None
