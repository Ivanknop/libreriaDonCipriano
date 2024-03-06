import sqlalchemy
from sqlalchemy import  Column, Integer, String, Date, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
import PyPDF2 as pdf
from PyPDF2 import PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
import re

# Crear el motor (engine) de la base de datos
engine = sqlalchemy.create_engine("sqlite:///don_cipriano.db")
base = declarative_base()


class Book(base):
    """Clase que representa un libro en la base de datos."""

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    subtitle = Column(String)
    author = Column(String, nullable=False)
    category = Column(String, nullable=False)
    supplier = Column(String)
    purchasevalue = Column(String)
    salevalue = Column(Float)
    editorial = Column(String)
    year = Column(Integer)
    count = Column(Integer)
    percentage = Column(Float)
    notes = Column(String)
    purchasedate = Column(Date)
    saledate = Column(Date, nullable=True) 
    photo = Column(String)

    # Métodos getters para los atributos
    # (Opcional, depende de la necesidad)

    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title}, author={self.author}, category={self.category})>"


def create_schema():
    """Crear las tablas en la base de datos."""
    base.metadata.create_all(engine)
    print("Esquema creado correctamente.")


def drop_schema():
    """Borrar todos las tablas existentes en la base de datos."""
    base.metadata.drop_all(engine)


def insert_book(title, author, category, subtitle=None, supplier=None, purchasevalue=None, salevalue=None,
                editorial=None, year=None, count=None, percentage=None, notes=None, purchasedate=None,
                saledate=None, photo=None):
    """Inserta un libro en la base de datos."""
    # Validación de datos
    if not title or not author or not category:
        print("Error: Se requieren los campos 'title', 'author' y 'category' para insertar un libro.")
        return

    # Crea una sesión
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Crea una nueva instancia de Book
    new_book = Book(title=title, subtitle=subtitle, author=author, category=category,
                    supplier=supplier, purchasevalue=purchasevalue, salevalue=salevalue,
                    editorial=editorial, year=year, count=count, percentage=percentage,
                    notes=notes, purchasedate=purchasedate, saledate=saledate, photo=photo)

    try:
        # Agrega la nueva instancia a la sesión
        session.add(new_book)
        # Guarda los cambios en la base de datos
        session.commit()
        print("Libro insertado correctamente.")
    except IntegrityError as e:
        session.rollback()
        print(f"Error de integridad al insertar el libro: {e}")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error al insertar el libro: {e}")
    finally:
        session.close()


def get_books(id=None, title=None, author=None, category=None):
    """
    Recupera libros de la base de datos basado en filtros opcionales.
    
    Args:
    - id: ID del libro a recuperar.
    - title: Título del libro a recuperar.
    - author: Autor del libro a recuperar.
    - category: Categoría del libro a recuperar.
    """
    # Crea una sesión
    Session = sessionmaker(bind=engine)
    with Session() as session:
        try:
            # Realiza la consulta basada en los filtros proporcionados
            query = session.query(Book)
            if id:
                query = query.filter(Book.id == id)
            if title:
                query = query.filter(Book.title == title)
            if author:
                query = query.filter(Book.author == author)
            if category:
                query = query.filter(Book.category == category)
                
            books = query.all()
            return books
        except SQLAlchemyError as e:
            print(f"Error al obtener libros: {e}")
            return []

def update_book(book_id, updated_values):
    """
    Actualiza un libro en la base de datos.
    
    Args:
    - book_id: ID del libro a actualizar.
    - updated_values: Diccionario con los valores actualizados.
    """
    # Crea una sesión
    Session = sessionmaker(bind=engine)
    with Session() as session:
        try:
            # Obtén el libro que deseas actualizar por su id
            book = session.query(Book).get(book_id)
            if book:
                # Actualiza los valores del libro con los proporcionados en updated_values
                for key, value in updated_values.items():
                    setattr(book, key, value)
                session.commit()
                print("Libro actualizado correctamente.")
            else:
                print(f"No se encontró ningún libro con el ID {book_id}.")
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error al actualizar el libro: {e}")


def delete_book_by_title(title):
    """
    Elimina un libro de la base de datos por su título.
    
    Args:
    - title: Título del libro a eliminar.
    """
    # Crea una sesión
    Session = sessionmaker(bind=engine)
    with Session() as session:
        try:
            # Busca el libro por título
            book_to_delete = session.query(Book).filter(Book.title == title).first()
            if book_to_delete:
                session.delete(book_to_delete)
                session.commit()
                print(f"Libro '{title}' eliminado correctamente.")
            else:
                print(f"No se encontró ningún libro con el título '{title}'.")
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error al eliminar el libro: {e}")


def show_all_books():
    """Muestra todos los libros de la base de datos."""
    # Recupera todos los libros de la base de datos
    return get_books()

    
def fill_database_from_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PdfReader(file)  # Usa PdfReader en lugar de PdfFileReader
            # Recorrer cada página del PDF
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                # Leer el texto de la página y procesar los datos
                text = page.extract_text()

                # Patrón para encontrar líneas que contienen información de libros
                pattern = r'\[(.*?)\]\s*\((.*?)\)\s*(.*?)\n'
                matches = re.findall(pattern, text)

                # Procesar cada coincidencia encontrada
                for match in matches:
                    title, author, category = match
                    # Insertar el libro en la base de datos
                    insert_book(title=title.strip(), author=author.strip(), category=category.strip())

        print("Base de datos actualizada desde el archivo PDF exitosamente.")

    except Exception as e:
        print(f"Error al llenar la base de datos desde el archivo PDF: {e}")


def database_to_pdf():
    # Obtener los libros de la base de datos
    books = show_all_books()

    # Crear un nuevo documento PDF
    pdf_filename = "books.pdf"
    pdf_document = SimpleDocTemplate(pdf_filename, pagesize=letter)

    # Crear una lista para almacenar los datos de los libros
    data = [['ID', 'Title', 'Author', 'Category']]

    # Agregar los datos de los libros a la lista
    for book in books:
        data.append([book.id, book.title, book.author, book.category])

    # Crear una tabla con los datos de los libros
    table = Table(data)

    # Estilo de la tabla
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])

    table.setStyle(style)

    # Agregar la tabla al documento PDF
    pdf_document.build([table])

    print(f"PDF generado correctamente: {pdf_filename}")

#create_schema()

# drop_schema()

