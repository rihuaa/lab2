import unittest
import array_list as array_list
import linked_list as linked_list
from array_list import enlarge
from array_list import shrink
from array_list import insert
from array_list import get
from array_list import contains
from array_list import search
from array_list import remove
from array_list import pop
from array_list import size
from array_list import ArrayList

class TestCase(unittest.TestCase):
    def test_enlarge(self):
        arr = ArrayList()
        x2_arr = array_list.enlarge(arr)
        self.assertEqual(arr == x2_arr, False)
        arr.arr = [0, 5, 6, 9]
        self.assertEqual(arr.arr[2], 6)

    def test_shrink(self):
        arr = ArrayList()
        x2_arr = shrink(arr)
        self.assertEqual(arr == x2_arr, False)
        self.assertRaises(IndexError, arr.shrink, arr )

    def test_insert(self):
        arr = ArrayList()
        insert(arr, 10, 0)
        insert(arr, 20, 1)
        b=insert(arr, 30, 2)
        # self.assertEqual(arr.arr[2], 10)

    def test_get(self):
        arr = ArrayList()
        arr.arr = [0, 5, 6, 9]
        # print(arr)
    # def test_get_max_empty(self):
    #     arr = []
    #     self.assertEqual(get_max(arr), None)
    #
    # def test_reverse(self):
    #     self.assertEqual(reverse("qweEerty"), "ytreEewq")
    #     self.assertEqual(reverse(""), "")
    #
    # def test_search(self):
    #     arr = [1,2,3,4,5]
    #     self.assertEqual(search(arr, 5), 4)
    #     arr = []
    #     self.assertEqual(search(arr, 5), None)
    #
    # def test_search_index_bounds(self):
    #     arr = [1,2,3,4,5]
    #     self.assertEqual(search(arr, 6), None)
    #
    # def test_fib(self):
    #     def fib_numbers(n):
    #         sequence = []
    #         for i in range(n+1):
    #             sequence.append(fib(i))
    #         return sequence
    #
    #     #this will test your fib function by calling it multiple times
    #     self.assertEqual(fib_numbers(10),
    #             [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
    #
    # def test_fib_init_terms(self):
    #     self.assertEqual(fib(1), 1)
    #     self.assertEqual(fib(2), 1)
    #
    # def test_fib_zero(self):
    #     self.assertEqual(fib(0), 0)
    #
    # def test_factorial(self):
    #     self.assertEqual(factorial_iter(3), 6)
    #     self.assertEqual(factorial_iter(3), factorial_rec(3))
    #
    # def test_factorial_lt2(self):
    #     self.assertEqual(factorial_iter(0), 1)
    #     self.assertEqual(factorial_iter(1), 1)
    #     self.assertEqual(factorial_rec(0), 1)
    #     self.assertEqual(factorial_rec(1), 1)

    # def test_factorial_1000(self):
    #     self.assertEqual(factorial_iter(1000), 0)
    #     self.assertEqual(factorial_rec(1000), 0)

def main():
    # execute unit tests
    unittest.main()

if __name__ == '__main__':
    # execute main() function
    main()
