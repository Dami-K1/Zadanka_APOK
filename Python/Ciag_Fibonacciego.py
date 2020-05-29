import unittest

# https://pl.wikipedia.org/wiki/Ci%C4%85g_Fibonacciego
# f(0) = 0
# f(1) = 1
# f(n) = f(n-1) + f(n-2):
#   f(2) = f(1) + f(0) = 1 + 0 = 1
#   f(3) = f(2) + f(1) = 1 + 1 = 2
#   f(4) = f(3) + f(2) = 2 + 1 = 3
#   f(5) = f(4) + f(3) = 3 + 2 = 5


# iteracyjnie - pętla
def fib_i(nr_elementu):
    if type(nr_elementu) != int or nr_elementu < 0:
        raise TypeError("Tylko liczby naturalne")
    if nr_elementu == 0:
        return 0
    if nr_elementu == 1:
        return 1
    fpp = 0
    fp = 1
    fb = 1
    for _ in range(2, nr_elementu + 1):
        fb = fp + fpp
        # przesuwamy wartosci dla potrzeb kolejnego obrotu
        fpp = fp
        fp = fb
    return fb  # == fp


# rekursywnie/rekurencyjnie:
# - https://pl.wikipedia.org/wiki/Rekurencja
# - https://www.w3schools.com/python/python_functions.asp#Recursion
def fib_r(nr_elementu):
    if type(nr_elementu) != int or nr_elementu < 0:
        raise TypeError("Tylko liczby naturalne")
    if nr_elementu == 0:
        return 0
    if nr_elementu == 1:
        return 1
    return fib_r(nr_elementu - 1) + fib_r(nr_elementu - 2)


# jednostkowe testy automatyczne
# https://docs.python.org/3/library/unittest.html#basic-example
class TestCwiczen(unittest.TestCase):

    def test_fib_i(self):
        # https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
        with self.assertRaises(TypeError):
            fib_i(-1)
        with self.assertRaises(TypeError):
            fib_i(0.5)
        with self.assertRaises(TypeError):
            fib_i(3.5)
        self.assertEqual(fib_i(0), 0)
        self.assertEqual(fib_i(1), 1)
        self.assertEqual(fib_i(2), 1)
        self.assertEqual(fib_i(3), 2)
        self.assertEqual(fib_i(4), 3)
        self.assertEqual(fib_i(5), 5)
        self.assertEqual(fib_i(11), 89)

    def test_fig_r(self):
        with self.assertRaises(TypeError):
            fib_r(-1)
        with self.assertRaises(TypeError):
            fib_r(0.5)
        with self.assertRaises(TypeError):
            fib_r(3.5)
        self.assertEqual(fib_r(0), 0)
        self.assertEqual(fib_r(1), 1)
        self.assertEqual(fib_r(2), 1)
        self.assertEqual(fib_r(3), 2)
        self.assertEqual(fib_r(4), 3)
        self.assertEqual(fib_r(5), 5)
        self.assertEqual(fib_r(11), 89)


unittest.main(module=__name__, verbosity=2)
