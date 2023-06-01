from functions import Competitors

competitors: list[Competitors] = []
points = []
f = open('fob2016.txt', 'r',)
for row in f:
    competitors.append(Competitors(row))

f.close()

print(f'3. feladat: Versenyzők száma: {len(competitors)}')

sumWoman = 0
for row in competitors:
    if row.category == 'Noi':
        sumWoman += 1

print(f'4. feladat: A női versenyzők aránya: {(sumWoman / len(competitors)) * 100:.2f}%')

maxWoman = None
i = 0
while maxWoman == None:
    if competitors[i].category == 'Noi':
        maxWoman = competitors[i]
    else:
        i += 1



for row in competitors:
    if row.category == "Noi":
        if row.points() > maxWoman.points():
            maxWoman = row

print('6. feladat: A bajnok női versenyző')
print(f'\tNév: {maxWoman.name}')
print(f'\tEgyesület: {maxWoman.team}')
print(f'\tÖsszpont: {maxWoman.points()}')

f = open('osszpontFF.txt', 'w')
for row in competitors:
    if row.category == 'Felnott ferfi':
        f.write(f'{row.name};{row.points()}\n')

f.close()

stat  = dict()
for row in competitors:
    if row.team in stat.keys():
        stat[row.team] += 1
    else:
        stat[row.team] = 1
print('8. feladat: Statisztika')
for key, value in stat.items():
    if value > 2:
        print(f'\t{key}: {value} fő')
