import datetime
class Bill():
    def __init__(self,aSellBooks):
        self._date = datetime.datetime.now().replace(microsecond=0)
        self._sellBooks = aSellBooks
    
    def getDate(self):
        return self._date
    def getSellBooks(self):
        return self._sellBooks
    def calculateValue(self):
        return sum(map(lambda book: book.getSaleValue(), self.getSellBooks()))