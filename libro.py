class Libro():
    def __init__(self,titulo,subtitulo,autor, editorial, proveedor, tematica, observaciones, precio):
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.autor = autor
        self.editorial = editorial
        self.proveedor = proveedor
        self.tematica = tematica
        self.observaciones = observaciones
        self.precio = precio
    def __str__(self) -> str:
        return f'{titulo},{subtitulo},{autor},{editorial},${precio},{tematica},{proveedor}'
    
    def getTitulo(self):
        return self.titulo
    def getSubtitulo(self):
        return self.subtitulo
    def getAutor(self):
        return self.autor
    def getEditorial(self):
        return self.editorial
    def getProveedor(self):
        return self.proveedor
    def getObservaciones(self):
        return self.observaciones
    def getTematica(self):
        return self.tematica
    def getPrecio(self):
        return self.precio
'''
titulo = "El Resplandor"
subtitulo =" "
autor = "Stephen King"
editorial ="Ariel"
proveedor = 'alguno'
tematica = "Literatura Universal"
precio = 200
unLibro = Libro (titulo,subtitulo,autor,editorial,proveedor,tematica,'nada',precio)

print (unLibro)'''