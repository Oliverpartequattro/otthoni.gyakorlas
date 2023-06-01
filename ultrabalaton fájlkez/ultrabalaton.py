from functions import Competitors
competitors: list[Competitors] = []

f = open('ub2017egyeni.txt', 'r', encoding='UTF-8')
f.readline()
for row in f:
    competitors.append(Competitors(row))

f.close()

print(f'3. feladat: Egyéni indulók: {len(competitors)} fő')

completed = 0
for row in competitors:
    if row.sex == 'noi' and row.percentage == 100:
        completed += 1

print(f'4. feladat: Teljesítették akik nők: {completed}')

name = input('5. feladat: Kérem a sportoló nevét: ')
i = 0
while i < len(competitors) and competitors[i].name != name:
    i += 1
if i < len(competitors):
    print(f'Indult egyéniben a sportoló? Igen')
    if competitors[i].percent == 100:
        print(f'Teljesítette a távot? Igen')
    else:
        print(f'Teljesítette a távot? Nem')
else:
    print(f'Indult egyéniben a sportoló? Nem')
    
firstman = None
i = 0
while firstman == None:
    if competitors[i].sex == 'ferfi':
        firstman = competitors[i]
    else:
        i += 1

firstwoman = None
i = 0
while firstwoman == None:
    if competitors[i].sex == 'noi':
        firstwoman = competitors[i]
    else:
        i += 1
sum = 0
count = 0
for row in competitors:
    if row.sex == 'ferfi' and row.percentage == 100:
        sum += row.time()
        count += 1

print(f'7. feladat: Átlagos idő: {sum/count} óra')

winman = firstman
i = 0
for row in competitors:
    if row.sex == 'ferfi' and row.percentage == 100 and row.time() < winman.time():
        winman = row
print(winman.name, winman.raceNum)

winwoman = firstwoman
i = 0
for row in competitors:
    if row.sex == 'noi' and row.percentage == 100 and row.time() < winwoman.time():
        winwoman = row
print(winwoman.name, winwoman.raceNum)
        
    



    
