from functions import Building

buildings: list[Building] = []

f = open('legmagasabb.txt', 'r', encoding='UTF-8')
for row in f:
    buildings.append(Building(row))
f.close()

print(f'3. feladat: {len(buildings)} van')
