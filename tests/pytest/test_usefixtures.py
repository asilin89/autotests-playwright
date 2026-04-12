import pytest


@pytest.fixture
def clear_books_db():
    print("[FIXTURE] - clearing DB")


@pytest.fixture
def fill_books_db():
    print("[FIXTURE] - filling DB")

# usefixtures() can be used when fixture result DO NOT RETURN anything
# cases: DB clear/fill, cache clear, upload test files etc.

@pytest.mark.usefixtures("fill_books_db")
def test_read_all_books_in_library():
    print("Reading all books in library")


@pytest.mark.usefixtures(
    "clear_books_db",
    "fill_books_db")
class TestLibrary:
    def test_read_book_from_library(self):
        print("Running test: test_read_book_from_library")

    def test_delete_book_from_library(self):
        print("Running test: test_delete_book_from_library")