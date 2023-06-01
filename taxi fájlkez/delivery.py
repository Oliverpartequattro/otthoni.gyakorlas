class Transport:
    def __init__(self, row) -> None:
        splittedData = row.strip().split(';')
        self.taxiId = splittedData[0]
        self.start = splittedData[1]
        self.duration = int(splittedData[2])
        self.distance = float(splittedData[3].replace(',', '.'))
        self.price = float(splittedData[4].replace(',', '.'))
        self.tip = float(splittedData[5].replace(',', '.'))
        self.paymentMethod = splittedData[6]