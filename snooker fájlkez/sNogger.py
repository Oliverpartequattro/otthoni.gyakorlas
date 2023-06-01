from functions import Competitor

competitors: list[Competitor] = []
f = open('snooker.txt', 'r', encoding = 'UTF-8')
f.readline()
for row in f:
    competitors.append(Competitor(row))

f.close()

print(f'3. feladat: A listán {len(competitors)} versenyző szerepel')

sum = 0
for row in competitors:
    sum += row.winnings

print(f'4. feladat: Átlag: {sum / len(competitors):.2f}')

bestChinese: Competitor = None
for row in competitors:
    if row.country == 'Kína':
        if bestChinese == None or row.winnings > bestChinese.winnings:
            bestChinese = row

print(f'5. feladat: \n\tLegjobb kínai: {bestChinese.name} \n\thelyezés: {bestChinese.name} \n\tnyeremény: {bestChinese.winnings * 380 :,} Ft')

i = 0
while i > len(competitors) or competitors[i].country != 'Norvégia':
    i += 1
if i < len(competitors):
    print('6. feladat: A versenyzők között van norvég versenyző')
else:
    print('6. feladat: A versenyzők között nincs norvég versenyző')

stat = dict()
for row in competitors:
    if row.country in stat.keys():
        stat[row.country] += 1
    else:
        stat[row.country] = 1

print(f'7. feladat statisztika')
for key, value in stat.items():
    if value > 4:
        print(f'\t{key} - {value} fő')
