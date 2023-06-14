firstWoman = None
for g in golf:
    if g.category == "Noi":
        firstWoman = g
        break

bestWoman = firstWoman
for g in golf:
    if g.category == "Noi" and g.points > bestWoman.points:
        bestWoman = g
