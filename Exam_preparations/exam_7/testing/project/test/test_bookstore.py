from unittest import TestCase

# from Exam_preparations.exam_7.testing.project.bookstore import Bookstore
from project.bookstore import Bookstore


class TestBookStore(TestCase):
    BOOKS_LIMIT = 2
    TEST_TITLE_1 = "Test1"
    TEST_TITLE_2 = "Test2"
    TEST_TITLE_3 = "Test3"
    TEST_VALUE_1 = 1
    TEST_VALUE_2 = 0
    TEST_VALUE_3 = 99

    def setUp(self) -> None:
        self.book_store = Bookstore(self.BOOKS_LIMIT)

    def test_init(self):
        self.assertEqual(self.BOOKS_LIMIT, self.book_store.books_limit)
        self.assertDictEqual({}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.book_store.total_sold_books)

    def test_books_limit_setter_zero(self):
        value = 0
        with self.assertRaises(ValueError) as ex:
            self.book_store.books_limit = value
        expected_result = f"Books limit of {value} is not valid"
        self.assertEqual(expected_result, str(ex.exception))

    def test_books_limit_setter_negative(self):
        value = -2
        with self.assertRaises(ValueError) as ex:
            self.book_store.books_limit = value
        expected_result = f"Books limit of {value} is not valid"
        self.assertEqual(expected_result, str(ex.exception))

    def test_len(self):
        self.book_store.availability_in_store_by_book_titles = {
            self.TEST_TITLE_1: self.TEST_VALUE_1,
            self.TEST_TITLE_2: self.TEST_VALUE_2
        }
        expected_result = self.TEST_VALUE_1 + self.TEST_VALUE_2
        actual_result = len(self.book_store)
        self.assertEqual(expected_result, actual_result)

    def test_receive_book_expect_to_raise(self):
        with self.assertRaises(Exception) as ex:
            self.book_store.receive_book(self.TEST_TITLE_1, self.TEST_VALUE_3)
        expected_result = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertDictEqual({}, self.book_store.availability_in_store_by_book_titles)

    def test_receive_book_happy_case(self):
        actual_result = self.book_store.receive_book(self.TEST_TITLE_1, self.TEST_VALUE_1)
        expected_result = f"{self.TEST_VALUE_1} copies of {self.TEST_TITLE_1} are available in the bookstore."
        self.assertEqual(expected_result, actual_result)
        self.assertDictEqual({self.TEST_TITLE_1: self.TEST_VALUE_1},
                             self.book_store.availability_in_store_by_book_titles)
        actual_result = self.book_store.receive_book(self.TEST_TITLE_1, self.TEST_VALUE_1)
        expected_result = f"{self.TEST_VALUE_1 * 2} copies of {self.TEST_TITLE_1} are available in the bookstore."
        self.assertEqual(expected_result, actual_result)
        self.assertDictEqual({self.TEST_TITLE_1: self.TEST_VALUE_1 * 2}, self.book_store.availability_in_store_by_book_titles)
        self.book_store.books_limit = 10
        actual_result = self.book_store.receive_book(self.TEST_TITLE_2, self.TEST_VALUE_1)
        expected_result = f"{self.TEST_VALUE_1} copies of {self.TEST_TITLE_2} are available in the bookstore."
        self.assertEqual(expected_result, actual_result)
        self.assertDictEqual({self.TEST_TITLE_1: self.TEST_VALUE_1 * 2, self.TEST_TITLE_2: self.TEST_VALUE_1},
                             self.book_store.availability_in_store_by_book_titles)

    def test_sell_book_expect_to_raise(self):
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book(self.TEST_TITLE_1, self.TEST_VALUE_1)
        expected_result = f"Book {self.TEST_TITLE_1} doesn't exist!"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertDictEqual({}, self.book_store.availability_in_store_by_book_titles)

    def test_sell_book_selling_more_than_having_expect_to_raise(self):
        self.book_store.availability_in_store_by_book_titles = {self.TEST_TITLE_1: self.TEST_VALUE_1}
        with self.assertRaises(Exception) as ex:
            self.book_store.sell_book(self.TEST_TITLE_1, self.TEST_VALUE_3)
        expected_result = f"{self.TEST_TITLE_1} has not enough copies to sell. Left: {self.TEST_VALUE_1}"
        self.assertEqual(expected_result, str(ex.exception))
        self.assertDictEqual({self.TEST_TITLE_1: self.TEST_VALUE_1}, self.book_store.availability_in_store_by_book_titles)

    def test_sell_book_happy_case(self):
        self.book_store.availability_in_store_by_book_titles = {self.TEST_TITLE_1: self.TEST_VALUE_1 * 2}
        actual_result = self.book_store.sell_book(self.TEST_TITLE_1, self.TEST_VALUE_1)
        expected_result = f"Sold {self.TEST_VALUE_1} copies of {self.TEST_TITLE_1}"
        self.assertEqual(expected_result, actual_result)
        self.assertDictEqual({self.TEST_TITLE_1: self.TEST_VALUE_1}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(self.TEST_VALUE_1, self.book_store.total_sold_books)

    def test_str(self):
        self.book_store.availability_in_store_by_book_titles = {self.TEST_TITLE_1: self.TEST_VALUE_1 * 2}
        self.book_store.sell_book(self.TEST_TITLE_1, self.TEST_VALUE_1)
        actual_result = str(self.book_store)
        expected_result = None
        result = [f"Total sold books: {self.book_store.total_sold_books}"]
        result.append(f'Current availability: {len(self.book_store)}')
        for book_title, number_of_copies in self.book_store.availability_in_store_by_book_titles.items():
            result.append(f" - {book_title}: {number_of_copies} copies")
        expected_result = '\n'.join(result)
        self.assertEqual(expected_result, actual_result)

