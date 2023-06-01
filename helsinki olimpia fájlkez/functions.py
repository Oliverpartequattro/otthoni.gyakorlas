class Result:
    def __init__(self, row:str) -> None:
        splittedData = row.strip().split(' ')
        self.rank = splittedData[0]
        self.people = int(splittedData[1])
        self.sport = splittedData[2]
        self.race = splittedData[3]
    
    def points(self):
        r = int(self.rank)
        #if r == 1:
        #    return 7
        #if r == 2:
        #    return 5
        #if r == 3:
        #    return 4
        #if r == 4:
        #    return 3
        #if r == 5:
        #    return 2
        #if r == 6:
            #return 1
        if r ==1:
            return 7
        else:
            return 7 - r
            