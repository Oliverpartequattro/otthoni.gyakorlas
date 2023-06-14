def vovel(day, vovels):
    count = 0
    for c in day:
        if c in vovels:
            count += 1
    return count
    
workdays = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']
vovels = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ü', 'ű', 'u', 'ú', "ö", "ő"]

bestday = [0, ""]

for day in workdays:
    if vovel(day, vovels) > bestday[0]:
        bestday[1] = day
        bestday[0] = vovel(day, vovels)

print(bestday[1])

        