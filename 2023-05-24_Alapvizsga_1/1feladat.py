print('1. feladat - a 3szög szerkeszthetősége')
print('A 3szög oldalai')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    print('A 3szög szereksszthető')
else:
    print('nem')