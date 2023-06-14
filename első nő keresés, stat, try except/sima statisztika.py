stat = {}
for g in golf:
    if g.association in stat.keys():
        stat[g.association] += 1
    else:
        stat[g.association] = 1

print(f". feladat: statisztika")
for key, value in stat.items():
    print(f"\t{key} - {value}")
