from delivery import Transport

transports: list[Transport] = []
f = open('fuvar.csv', 'r', encoding = 'UTF - 8')
f.readline()
for row in f:
    transports.append(Transport(row))

f.close()

print(f'3. feladat: {len(transports)} fuvar')

count = 0
sum = 0
for t in transports:
    if t.taxiId == '6185':
        count += 1
        sum += t.price + t.tip

print(f'4. feladat {count} fuvar alatt {sum} dollár')

stat = dict()
for t in transports:
    if t.paymentMethod in stat.keys():
        stat[t.paymentMethod] += 1
    else:
        stat[t.paymentMethod] = 1

print('5. feladat:')
print('5. feladat:')
for key, value in stat.items():
    print(f'\t{key}: {value} fuvar')

sum = 0
for t in transports:
    sum += t.distance

print(f'6. feladat: {sum * 1.6:.2f} km')

longestTransport = transports[0]
for t in transports:
    if t.duration > longestTransport.duration:
        longestTransport = t 

print('7. feladat:')
print(f'\tFuvar hossza: {longestTransport.duration} másodperc')
print(f'\tTaxi azonosító: {longestTransport.taxiId}')
print(f'\tMegtett távolság: {longestTransport.distance * 1.6:.2f} km')
print(f'\tViteldíj: {longestTransport.price}$')

print('8. feladat: hibák.txt')
f = open('hibak.txt', 'w', encoding='UTF-8')
f.write('taxi_id;indulas;idotartam;tavolsag;viteldij;borravalo;fizetes_modja\n')

for t in transports:
    if t.distance == 0 and t.price > 0 and t.duration > 0:
        f.write(f'{t.taxiId};{t.start};{t.duration};{t.distance};{t.price};{t.tip};{t.paymentMethod}')
f.close()
