print('LNKO kivonásos algoritmussal')

def lnko(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


a = int(input("a = "))
b = int(input("b =  "))

lnko = lnko(a, b)

print(f'LNKO({a},{b}) = {lnko}')



    