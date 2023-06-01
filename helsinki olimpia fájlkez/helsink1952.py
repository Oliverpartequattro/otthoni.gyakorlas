from functions import Result

olimpics: list[Result] = []
f = open('helsinki.txt', 'r',)
for row in f:
    olimpics.append(Result(row))
f.close()

print('3. feladat:')
print(f'Pontszerző helyezések száma: {len(olimpics)}')

gold = 0
silver = 0
bronze = 0
for row in olimpics:
    if row.rank == '1':
        gold += 1
    elif row.rank == '2':
        silver += 1
    elif row.rank == '3':
        bronze += 1
    else:
        pass

print('4. feladat:')
print(f'Arany: {gold}')
print(f'Ezüst: {silver}:')
print(f'Bronza: {bronze}')
print(f'Összesen: {gold + silver + bronze}')

sum = 0
for row in olimpics:
    sum += row.points()

print(f'5. feladat:')
print(f'Olimpiai pontok sASDASDASDASDSDOSELESZVÉGEzáma: {sum}')

swim = 0
gym = 0

for row in olimpics:
    if row.sport == 'uszas' and row.rank <= '3':
        swim += 1
    elif row.sport == 'torna' and row.rank <= '3':
        gym += 1

if gym > swim:
    print('6. feladat:\nTornában szereztek több érmet')
elif swim > gym:
    print('Ilyen meg nincs')
else:
    print('Ilyen se')

f = open('helsinki2.txt', 'w')
for row in olimpics:
    f.write("{0} {1} {2} {3} {4}\n".format(\
        row.rank,\
        row.people,\
        row.points(),\
        row.sport.replace('kajakkenu', 'kajak-kenu'),\
        row.race))
f.close()

ArithmeticError = True

max = olimpics[0]
for row in olimpics:
    if row.people > max.people:
        max = row

print('8. feladat:')
print(f'Helyezés: {max.rank}')
print(f'Sportág: {max.sport}')
print(f'Versenyszám: {max.race}')
print(f'Emberek: {max.people}')

