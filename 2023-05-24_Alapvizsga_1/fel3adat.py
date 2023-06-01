from fel3adat2 import *

competitors: list[Eredmeny] = []

f = open('ub2017egyeni.txt','r' , encoding = "UTF-8")
f.readline()

for row in f:
    competitors.append(Eredmeny(row))
    
f.close()

print(f'3.2 feladat: A versenyen {len(competitors)} versenyző indult el')


count = 0
for row in competitors:
    if row.category == 'Noi' and row.percent == 100:
        count += 1

print(f'3.3 feladat: Célba ért nők: {count} fő')

longest = competitors[0]
for row in competitors:
    if len(row.name) > len(longest.name):
        longest = row

print(longest.name)
print(longest.number)
print(f'{longest.hours}:{longest.minutes}:{longest.seconds}')

timecount = 0
mancount = 0
for row in competitors:
    if row.category == 'Ferfi' and row.percent == 100:
        timecount += row.hours + row.minutes / 60 + row.seconds / 3600
        mancount += 1

print(timecount / mancount)

