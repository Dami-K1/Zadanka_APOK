import unittest


# https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego
def tribonacci(nr_elementu):
    if type(nr_elementu) != int or nr_elementu < 0:
        raise TypeError("Tylko liczby naturalne")
    if nr_elementu == 0:
        return 0
    if nr_elementu == 1:
        return 0
    if nr_elementu == 2:
        return 1
    return tribonacci(nr_elementu - 1) + tribonacci(nr_elementu - 2) + tribonacci(nr_elementu - 3)


# zaimplementuj funkcję n-bonacci, która jest uogólnieniem fibonacciego, tribonacciego itd:
# funkcja liczy zadany element ciągu:
# dla n=2 fibonacciego,
# dla n=3 tribonaciego,
# ...
def nbonacci(n, nr_elementu):
    if type(n) != int or n < 2:
        raise TypeError("n musi byc naturalne i nie mniejsze niz 2")
    if type(nr_elementu) != int or nr_elementu < 0:
        raise TypeError("nr elementu musi byc liczba naturalna")
    if nr_elementu+1 < n:
        return 0
    if nr_elementu+1 == n:
        return 1
    nval = 0
    for i in range(1, n+1):
        nval += nbonacci(n, nr_elementu - i)
    return nval


# jednostkowe testy automatyczne
# https://docs.python.org/3/library/unittest.html#basic-example
class TestCwiczen(unittest.TestCase):

    def test_tribonacci(self):
        with self.assertRaises(TypeError):
            tribonacci(-1)
        with self.assertRaises(TypeError):
            tribonacci(0.5)
        with self.assertRaises(TypeError):
            tribonacci(3.5)
        self.assertEqual(tribonacci(0), 0)
        self.assertEqual(tribonacci(1), 0)
        self.assertEqual(tribonacci(2), 1)
        self.assertEqual(tribonacci(3), 1)
        self.assertEqual(tribonacci(4), 2)
        self.assertEqual(tribonacci(5), 4)
        self.assertEqual(tribonacci(11), 149)

    def test_nbonacci(self):
        with self.assertRaises(TypeError):
            nbonacci(-1, 3)
        with self.assertRaises(TypeError):
            nbonacci(1, 3)
        with self.assertRaises(TypeError):
            nbonacci(3.5, 3)
        with self.assertRaises(TypeError):
            nbonacci(2, -1)
        with self.assertRaises(TypeError):
            nbonacci(2, 0.5)
        with self.assertRaises(TypeError):
            nbonacci(2, 3.5)
        # fibonacci
        self.assertEqual(nbonacci(2, 0), 0)
        self.assertEqual(nbonacci(2, 1), 1)
        self.assertEqual(nbonacci(2, 1), 1)
        self.assertEqual(nbonacci(2, 11), 89)
        # tribonacci
        self.assertEqual(nbonacci(3, 0), 0)
        self.assertEqual(nbonacci(3, 1), 0)
        self.assertEqual(nbonacci(3, 2), 1)
        self.assertEqual(nbonacci(3, 3), 1)
        self.assertEqual(nbonacci(3, 4), 2)
        self.assertEqual(nbonacci(3, 11), 149)
        # tetranacci
        self.assertEqual(nbonacci(4, 0), 0)
        self.assertEqual(nbonacci(4, 1), 0)
        self.assertEqual(nbonacci(4, 2), 0)
        self.assertEqual(nbonacci(4, 3), 1)
        self.assertEqual(nbonacci(4, 4), 1)
        self.assertEqual(nbonacci(4, 5), 2)
        self.assertEqual(nbonacci(4, 11), 108)
        # 5-nacci
        self.assertEqual(nbonacci(5, 0), 0)
        self.assertEqual(nbonacci(5, 1), 0)
        self.assertEqual(nbonacci(5, 2), 0)
        self.assertEqual(nbonacci(5, 3), 0)
        self.assertEqual(nbonacci(5, 4), 1)
        self.assertEqual(nbonacci(5, 5), 1)
        self.assertEqual(nbonacci(5, 6), 2)
        self.assertEqual(nbonacci(5, 11), 61)


unittest.main(module=__name__, verbosity=2)
