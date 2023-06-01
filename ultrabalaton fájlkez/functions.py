class Competitors:
    def __init__(self, row:str) -> None:
        splittedData = row.strip().split(';')
        self.name = splittedData[0]
        self.raceNum = splittedData[1]
        self.sex = splittedData[2].lower()
        time = splittedData[3].split(':')
        self.hours = int(time[0])
        self.minutes = int(time[1])
        self.seconds = int(time[2])
        self.percentage = int(splittedData[4])

    def time(self):
        hourtime = self.hours + (self.minutes / 60) + (self.seconds / 3600)
        return hourtime