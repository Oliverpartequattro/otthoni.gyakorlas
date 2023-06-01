class Fullplate:
    def __init__(self, row:str) -> None:
        splittedData = row.strip().split(';') #Fajta;Megnevezés;Ár;Rendelt mennyiség
        self.type = splittedData[0]
        self.name = splittedData[1]
        self.price = int(splittedData[2])
        self.ordered = int(splittedData[3])
        