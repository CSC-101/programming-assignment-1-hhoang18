import data
import hw1
import unittest

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_1(self):
        input = "Hello"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    def test_vowel_2(self):
        input = "World"
        result = hw1.vowel_count(input)
        expected = 1
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists_1(self):
        input = [[1,2],[3,4,5],[6,7,8]]
        result = hw1.short_lists(input)
        expected = [[1,2]]
        self.assertEqual(expected, result)

    def test_short_lists_2(self):
        input = [[2,3,4,5],[6,3],[7,6]]
        result = hw1.short_lists(input)
        expected = [[6,3],[7,6]]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs_1(self):
        input = [[6,5],[7,8,9]]
        result = hw1.ascending_pairs(input)
        expected = [[5,6],[7,8,9]]
        self.assertEqual(expected, result)

    def test_ascending_pairs_2(self):
        input = [[3,4,2],[4,2],[8,3]]
        result = hw1.ascending_pairs(input)
        expected = [[3,4,2],[2,4],[3,8]]
        self.assertEqual(expected, result)

    # Part 4
    def test_add_prices_1(self):
        price1=data.Price(5,80)
        price2=data.Price(2,30)
        result = hw1.add_prices(price1,price2)
        expected = data.Price(8,10)
        self.assertEqual(expected, result)

    def test_add_prices_2(self):
        price1 = data.Price(3, 40)
        price2 = data.Price(1, 60)
        result = hw1.add_prices(price1,price2)
        expected = data.Price(5,0)
        self.assertEqual(expected, result)

    # Part 5
    def test_rectangle_1(self):
        input = data.Rectangle(data.Point(4,2),data.Point(0,6))
        result = hw1.rectangle_area(input)
        expected = 16
        self.assertEqual(expected, result)

    def test_rectangle_2(self):
        input = data.Rectangle(data.Point(2, 6), data.Point(4, 2))
        result = hw1.rectangle_area(input)
        expected = 8
        self.assertEqual(expected, result)

    # Part 6
    def test_books_1(self):
        author_name = "Rick Riordan"
        books = [data.Book(["Suzanne Collins"], "The Hunger Games"),
            data.Book(["Rick Riordan"], "The Sea of Monsters")]
        result = hw1.books_by_author(author_name, books)
        expected = [data.Book(["Rick Riordan"], "The Sea of Monsters")]
        self.assertEqual(expected, result)

    def test_books_2(self):
        author_name = "Naomi Novik"
        books = [data.Book(["Suzanne Collins"], "The Hunger Games"),
            data.Book(["Naomi Novik"], "A Deadly Education")]
        result = hw1.books_by_author(author_name, books)
        expected = [data.Book(["Naomi Novik"], "A Deadly Education")]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_1(self):
        input = data.Rectangle(data.Point(3, 4), data.Point(9, 12))
        result = hw1.circle_bound(input)
        expected_center = data.Point(6, 8)
        expected_radius = 5
        expected = data.Circle(data.Point(6,8), 5)
        self.assertEqual(expected.center, result.center)

    def test_circle_2(self):
        input = data.Rectangle(data.Point(0, 1), data.Point(2, 7))
        result = hw1.circle_bound(input)
        expected_center = data.Point(1, 4)
        expected_radius = 2
        expected = data.Circle(data.Point(1,4), 2)
        self.assertEqual(expected.center, result.center)

    # Part 8
    def test_below_pay_1(self):
        input = [data.Employee("Bob",8),data.Employee("Sam",10)]
        result = hw1.below_pay_average(input)
        expected = ["Bob"]
        self.assertEqual(expected, result)

    def test_below_pay_2(self):
        input = [data.Employee("Tony",15),data.Employee("Melissa",9)]
        result = hw1.below_pay_average(input)
        expected = ["Melissa"]
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
