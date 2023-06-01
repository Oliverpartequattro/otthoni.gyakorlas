class Competitor:
    def __init__(self, row) -> None:
        splittedData = row.strip().split(';')
        self.position = int(splittedData[0])
        self.name = splittedData[1]
        self.country = splittedData[2]
        self.winnings = int(splittedData[3])
        