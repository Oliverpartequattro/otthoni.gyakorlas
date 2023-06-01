class Fuel:
    def __init__(self, row:str) -> None:
        splittedData = row.strip().split(';')
        self.year = int(splittedData[0].split('.')[0])
        self.month = int(splittedData[0].split('.')[1])
        self.day = int(splittedData[0].split('.')[2])
        self.petrol = int(splittedData[1])
        self.diesel = int(splittedData[2])
