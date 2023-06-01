from functions import Fuel

def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
prices: list[Fuel] = []

def daysBetweenChanges(p1: prices, p2:prices):
    daysOfMonths = [31,28,31,30,31,30,31,31,30,31,30,31]
    if p1.leap_year():
        daysOfMonths[1] = 29
    if p1.month == p2.month:
        return abs(p1.day - p2.day)
    elif p1.month < p2.month:   
        return daysOfMonths[p1.month - 1] - p1.day + p2.day
    else:
        return daysOfMonths[p2.month - 1] - p2.day + p1.day

f = open('uzemanyag.txt', 'r', encoding='UTF-8')
for row in f:
    prices.append(Fuel(row))
f.close()

print(f'3. feladat: {len(prices)} alkalomszor történt változás')

minDiff = abs(prices[0].petrol - prices[0].diesel) 
count = 0
for row in prices:
    if abs(row.petrol - row.diesel) <= minDiff:
        if minDiff == 0:
            count += 1
        minDiff =  abs(row.petrol - row.diesel)

print(f'4. feladat: A legkisebb különbség: {minDiff}')
print(f'5. feladat: {count + 1} alkalommal fordult elő')

leapyr = []
for i in range(1900, 3000):
    if i % 4 == 0:
        leapyr.append(i)

count = 0
for row in prices:
    if row.year % 4 == 0 and row.month == 2 and row.day == 24:
        count += 1

if count > 0:
    print(f'6. feladat: Volt változás szökőnapon')
else:
    print('Nem volt')

euro = 307.7
f = open('euro.txt', 'w', encoding = 'UTF-8')
for row in prices:
    f.write(f'{row.year}.{row.month}.{row.day};{row.petrol / euro:.2f};{row.diesel / euro:.2f}\n')
f.close()

yearnumber = int(input('§Évszám§ '))
while yearnumber > 2016 or yearnumber < 2011:
    yearnumber = int(input('§Évszám§ '))

i = 0
while prices[i].year != yearnumber:
    i += 1

maxDays = daysBetweenChanges(prices[i], prices[i+1])
i += 1
while prices[i+1].year == yearnumber:
    if daysBetweenChanges(prices[i],prices[i+1]) > maxDays:
        maxDays = daysBetweenChanges(prices[i], prices[i+1])
    i += 1

print(f'10. feladat: {yearnumber} évben az leghosszabb időszak {maxDays} nap volt.')
