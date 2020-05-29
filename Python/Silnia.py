import unittest

# https://pl.wikipedia.org/wiki/Silnia


# iteracyjnie - pętla
def silnia_i(liczba):
    s = 1
    for i in range(2, liczba + 1):
        s = s * i
    return s


def silnia_i_m(liczba):
    if liczba < 0:
        return 0, False, "Liczba musi byc wieksza lub równa 0"
    s = 1
    for i in range(2, liczba + 1):
        s = s * i
    return s, True, ""


def silnia_i_e(liczba):
    if liczba < 0:
        raise NameError("Liczba musi byc wieksza lub równa 0")
    s = 1
    for i in range(2, liczba + 1):
        s = s * i
    return s


# rekursywnie/rekurencyjnie:
# - https://pl.wikipedia.org/wiki/Rekurencja
# - https://www.w3schools.com/python/python_functions.asp#Recursion

def silnia_r(liczba):
    if liczba == 0:
        return 1
    else:
        return silnia_r(liczba-1)*liczba


def silnia_r_m(liczba):
    if liczba < 0:
        return 0, False, "Liczba musi byc wieksza niz 0!"
    if liczba == 0:
        return 1, True, ""
    else:
        s, _, _ = silnia_r_m(liczba - 1)
        return s*liczba, True, ""


def silnia_r_e(liczba):
    if liczba < 0:
        raise NameError('Liczba musi byc wieksza niz 0!')
    if liczba == 0:
        return 1
    else:
        return silnia_r(liczba-1)*liczba


# jednostkowe testy automatyczne
# https://docs.python.org/3/library/unittest.html#basic-example
class TestCwiczen(unittest.TestCase):
    def test_silnia_iteracyjna(self):
        self.assertEqual(silnia_i(0), 1)
        self.assertEqual(silnia_i(1), 1)
        self.assertEqual(silnia_i(2), 2)
        self.assertEqual(silnia_i(3), 6)
        self.assertEqual(silnia_i(10), 3628800)

    def test_silnia_rekurencyjna(self):
        self.assertEqual(silnia_r(0), 1)
        self.assertEqual(silnia_r(1), 1)
        self.assertEqual(silnia_r(2), 2)
        self.assertEqual(silnia_r(3), 6)
        self.assertEqual(silnia_r(10), 3628800)

    def test_silnia_bl(self):
        s, ok, opis_bl = silnia_i_m(-1)
        print("silnia_bl: ", s, ok, opis_bl)

    def test_silnia_ex(self):
        try:
          s = silnia_i_e(1)
          print("silnia_ex: ", s)
        except NameError as err:
          print("silnia_ex: ", err)


unittest.main(module=__name__, verbosity=2)
