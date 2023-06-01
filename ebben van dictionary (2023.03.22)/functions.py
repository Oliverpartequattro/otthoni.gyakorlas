class Competitors:
    def __init__(self, row:str) -> None:
        splittedData = row.strip().split(';')
        self.name = splittedData[0]
        self.category = splittedData[1]
        if splittedData[2] == 'n.a.':
            self.team = 'nincs csapata'
        else:
            self.team = splittedData[2]
        self.points1 = int(splittedData[3])
        self.points2 = int(splittedData[4])
        self.points3 = int(splittedData[5])
        self.points4 = int(splittedData[6])
        self.points5 = int(splittedData[7])
        self.points6 = int(splittedData[8])
        self.points7 = int(splittedData[9])
        self.points8 = int(splittedData[10])
        self.pointsSum = self.points1 + self.points2 + self.points3 + self.points4 + self.points5 + self.points6 + self.points7 + self.points8

    def points(self):
        points = []
        sumPoints = 0
        points.append(self.points1)
        points.append(self.points2)
        points.append(self.points3)
        points.append(self.points4)
        points.append(self.points5)
        points.append(self.points6)
        points.append(self.points7)
        points.append(self.points8)
        points.sort()
        for i in range(2):
            if points[0] != 0:
                sumPoints += 10
            points.pop(0)
        sumPoints += points[0]
        sumPoints += points[1]
        sumPoints += points[2]
        sumPoints += points[3]
        sumPoints += points[4]
        sumPoints += points[5]

        return sumPoints