import unittest
from book import Book
from bill import Bill

class TestAdminPook_db(unittest.TestCase):
    def testAddBook(self):
        books = []
        book_dict = {'title':'El Resplandor','author':'King','subTitle':'','photo':'','percentage':100,'notes':'','purchaseDate':12/12/2023,'saleDate':'01/02/2024','count':1,'editorial':'RBA','supplier':'Propio','category':'Literatura Univesal','purchaseValue':0,'saleValue':100,'year':2000}
        book = Book(book_dict)  
        books.append(book)     
        self.assertEqual(len(books),1)
        self.assertEqual(book.getTitle(),'El Resplandor')


    def testEditBook(self):
        book_dict = {'title':'El Resplandor','author':'King','subTitle':'','photo':'','percentage':100,'notes':'','purchaseDate':12/12/2023,'saleDate':'01/02/2024','count':1,'editorial':'RBA','supplier':'Propio','category':'Literatura Univesal','purchaseValue':0,'saleValue':100,'year':2000}
        book = Book(book_dict)     
        self.assertEqual(book.getCount(),1)
        newBookDict = {'title':'El Resplandor','author':'King','subTitle':'','photo':'','percentage':100,'notes':'','purchaseDate':12/12/2023,'saleDate':'01/02/2024','count':0,'editorial':'RBA','supplier':'Propio','category':'Literatura Univesal','purchaseValue':0,'saleValue':100,'year':2000}   
        newBook = Book(newBookDict)
        book.synchronize(newBook)
        self.assertEqual(book.getCount(),0)

    def testSellOneBook(self):
        books = []
        book_dict = {'title':'El Resplandor','author':'King','subTitle':'','photo':'','percentage':100,'notes':'','purchaseDate':12/12/2023,'saleDate':'01/02/2024','count':1,'editorial':'RBA','supplier':'Propio','category':'Literatura Univesal','purchaseValue':0,'saleValue':100,'year':2000}
        book = Book(book_dict) 
        books.append(book)      
        newBookDict = {'title':'El Hobbit','author':'Tolkien','subTitle':'','photo':'','percentage':100,'notes':'','purchaseDate':12/12/2023,'saleDate':'01/02/2024','count':0,'editorial':'RBA','supplier':'Propio','category':'Literatura Univesal','purchaseValue':0,'saleValue':150,'year':2001}   
        newBook = Book(newBookDict)
        books.append(newBook)     
        self.assertEqual(len(books),2)
        bill = Bill(books)
        self.assertEqual(bill.calculateValue(),250)
        
if __name__ == '__main__':
    unittest.main()