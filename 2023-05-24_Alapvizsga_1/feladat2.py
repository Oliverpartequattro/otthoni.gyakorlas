def tokeletes_e(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number

tokeletesnumber=[]

print("2. feladat: Tökéletes számok")
    
print("Kérek 2 termszámot")

tol = int(input('tól '))
ig = int(input('ig '))

for i in range(tol, ig + 1):
    if tokeletes_e(i):
        tokeletesnumber.append(str(i)) #hogy ki lehessen irni normalisan
        
        
if len(tokeletesnumber) <= 0:
    print('nincs')
else:
    print('; '.join(tokeletesnumber))
        