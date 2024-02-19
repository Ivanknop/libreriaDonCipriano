class Book():
    def __init__(self,aBookValues):
        self.title = aBookValues['title']
        self.subTitle = aBookValues['subTitle']
        self.author = aBookValues['author']
        self.category = aBookValues['category']
        self.supplier = aBookValues['supplier']
        self.purchaseValue = aBookValues['purchaseValue']
        self.saleValue = aBookValues['saleValue']
        self.editorial = aBookValues['editorial']
        self.year = aBookValues['year']
        self.count = aBookValues['count']
        self.percentage = aBookValues['percentage']
        self.notes = aBookValues['notes']
        self.purchaseDate = aBookValues['purchaseDate']
        self.saleDate = aBookValues['saleDate']
        self.photo = aBookValues['photo']
    
    def getTitle(self):
        return self.title
    def getSubTitle(self):
        return self.subTitle
    def getAuthor(self):
        return self.author
    def getCategory(self):
        return self.category
    def getSupplier(self):
        return self.supplier
    def getPurchaseValue(self):
        return self.purchaseValue
    def getSaleValue(self):
        return self.saleValue 
    def getEditorial(self):
        return self.editorial
    def getYear(self):
        return self.year
    def getCount(self):
        return self.count
    def getPercentage(self):
        return self.percentage
    def getNotes(self):
        return self.notes
    def getPurchaseDate(self):
        return self.purchaseDate
    def getSaleDate(self):
        return self.saleDate
    def getPhoto(self):
        return self.photo
    
    def __str__(self):
        return (
            f'Título: {self.title}\n'
            f'Subtítulo: {self.subTitle}\n'
            f'Autor: {self.author}\n'
            f'Categoría: {self.category}\n'
            f'Proveedor: {self.supplier}\n'
            f'Valor de compra: {self.purchaseValue}\n'
            f'Valor de venta: {self.saleValue}\n'
            f'Editorial: {self.editorial}\n'
            f'Año: {self.year}\n'
            f'Cantidad: {self.count}\n'
            f'Porcentaje: {self.percentage}\n'
            f'Notas: {self.notes}\n'
            f'Fecha de compra: {self.purchaseDate}\n'
            f'Fecha de venta: {self.saleDate}\n'
        )
    
    def synchronize(self, aNewBook):
        self.title = aNewBook.getTitle()
        self.subTitle = aNewBook.getSubTitle()
        self.author = aNewBook.getAuthor()
        self.category = aNewBook.getCategory()
        self.supplier = aNewBook.getSupplier()
        self.purchaseValue = aNewBook.getPurchaseValue()
        self.saleValue = aNewBook.getSaleValue()
        self.editorial = aNewBook.getEditorial()
        self.year = aNewBook.getYear()
        self.count = aNewBook.getCount()
        self.percentage = aNewBook.getPercentage()
        self.notes = aNewBook.getNotes()
        self.purchaseDate = aNewBook.getPurchaseDate()
        self.saleDate = aNewBook.getSaleDate()
        self.photo = aNewBook.getPhoto()
    

