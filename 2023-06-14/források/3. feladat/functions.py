class Building:
    def __init__(self, row:str) -> None:
        splittedData = row.strip().split(';')
        self.name = splittedData[0]
        self.city = splittedData[1]
        self.country = splittedData[2]
        self.height = splittedData[3]
        self.floor = splittedData[4]
        self.year = splittedData[5]