class Eredmeny:
    def __init__(self, row) -> None:
        splittedData =row.strip().split(';')
        self.name = splittedData[0]
        self.number = splittedData[1]
        self.category = splittedData[2]
        self.hours = int(splittedData[3].split(':')[0])
        self.minutes = int(splittedData[3].split(':')[1])
        self.seconds = int(splittedData[3].split(':')[2])
        self.percent = int(splittedData[4])