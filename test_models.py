import unittest
from models import create_schema, insert_book, delete_book_by_title, get_books, update_book, drop_schema

class TestBookDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Configurar una base de datos de prueba una vez para todas las pruebas
        create_schema()

    def setUp(self):
        # Configurar una base de datos de prueba antes de cada prueba
        pass

    def test_insert_and_get_book(self):
        insert_book("Title 1", "Author 1", "Category 1")
        books = get_books(title="Title 1")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Title 1")
        self.assertEqual(books[0].author, "Author 1")
        self.assertEqual(books[0].category, "Category 1")

    def test_update_book(self):
        insert_book("Title 2", "Author 2", "Category 2")
        update_book(1, {"title": "Updated Title"})
        book = get_books(id=1)[0]
        self.assertEqual(book.title, "Updated Title")

    def test_delete_book(self):
        insert_book("Title 3", "Author 3", "Category 3")
        delete_book_by_title("Title 3")
        books = get_books(title="Title 3")
        self.assertEqual(len(books), 0)

    def test_get_books_by_author(self):
        insert_book("Title 4", "Author 4", "Category 4")
        books = get_books(author="Author 4")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].author, "Author 4")

    def test_get_books_by_category(self):
        insert_book("Title 5", "Author 5", "Category 5")
        books = get_books(category="Category 5")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].category, "Category 5")

    def test_insert_book_with_missing_fields(self):
        # Debería manejar correctamente la inserción de un libro con campos faltantes
        insert_book("Incomplete Title", "", "Category 6")
        books = get_books(title="Incomplete Title")
        self.assertEqual(len(books), 0)

    def test_update_nonexistent_book(self):
        # Debería manejar correctamente la actualización de un libro que no existe
        update_book(1000, {"title": "Nonexistent Title"})
        books = get_books(title="Nonexistent Title")
        self.assertEqual(len(books), 0)

    def test_delete_nonexistent_book(self):
        # Debería manejar correctamente la eliminación de un libro que no existe
        delete_book_by_title("Nonexistent Title")
        books = get_books(title="Nonexistent Title")
        self.assertEqual(len(books), 0)

    @classmethod
    def tearDownClass(cls):
        # Limpiar la base de datos de prueba al finalizar todas las pruebas
        drop_schema()

if __name__ == '__main__':
    unittest.main()
