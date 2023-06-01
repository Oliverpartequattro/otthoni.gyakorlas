from functions import Fullplate

food: list[Fullplate] = []

f = open('teletal.csv', 'r', encoding = 'UTF-8')
f.readline()
for row in f:
    food.append(Fullplate(row))
f.close()

print(f'{len(food)} étel')

count = 0
for row in food:
    if row.type == 'Főétel':
        count += 1
print(f'{count} főétel')

minfood = food[0]
for row in food:
    if row.price < minfood.price:
        minfood = row
print(minfood.name)

firstmenu = None
i = 0
while firstmenu == None:
    if food[i].type == 'Menü':
        firstmenu = food[i]
    else:
        i += 1
print(f'{firstmenu.name} első menü')

minmenu = firstmenu
for row in food:
    if row.type == 'Menü' and row.price < minmenu.price:
        minmenu = row 
    print(f'{minmenu.name} legolcsóbb menü')

sum = 0
for row in food:
    if row.type == 'Főétel':
        sum += row.price * row.ordered
        
print(f'Összes árbevétel: {sum / 402.5:.2f} eur')
        
stat  = dict()
for row in food:
    if row.type in stat.keys():
        stat[row.type] += row.ordered
    else:
        stat[row.type] = row.ordered
print('8. feladat: Statisztika')
for key, value in stat.items():
        print(f'{key}: {value} db')

money = int(input('Mennyi pézed van'))
f = open('budget.txt', 'w', encoding = 'UTF-8')
f.write('Megöllek\n')
for row in food:
    if row.price <= money:
        f.write(f'{row.type}, {row.name}, {row.price}\n')
f.close()
    