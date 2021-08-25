class Sistema():
    def __init__(self):
        self.libros = []
        self.proveedores = []
        self.facturas = []
    
    def getLibros(self):
        return self.libros
    def getProveedores (self):
        return self.proveedores
    def getFacturas (self):
        return self.facturas
    
    def agregarLibro (self,unLibro):
        self.libros.append(unLibro)
    def agregarProveedor(self,unProveedor):
        self.proveedores.append(unProveedor)
    def agregarFactura (self,unaFactura):
        self.facturas.append(unaFactura)