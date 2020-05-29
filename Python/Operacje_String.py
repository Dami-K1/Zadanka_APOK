import unittest


def zmien_znaki_1(znaki):
    return znaki.upper()


def zmien_znaki_2(znaki):
    znaki_w = ""
    i = 1
    for ch in znaki:
        if i % 2 == 0:
            ch = ch.upper()
        znaki_w = znaki_w + ch
        i = i + 1
    return znaki_w


def zmien_znaki_3(znaki):
    znaki_w = ""
    czy_parzysty = False
    for ch in znaki:
        if czy_parzysty:
            ch = ch.upper()
        znaki_w = znaki_w + ch
        czy_parzysty = not czy_parzysty
    return znaki_w


def zmien_znaki_4(znaki):
    znaki_w = ""
    poprzedni_znak = " "
    for ch in znaki:
        if poprzedni_znak == " ":
            ch = ch.upper()
        znaki_w = znaki_w + ch
        poprzedni_znak = ch
    return znaki_w


def zmien_znaki_na_poz(znaki, poz):
    znaki_w = ""
    iw = 1
    for ch in znaki:
        if ch == " ":
            iw = 0
        if iw == poz:
            ch = ch.upper()
        znaki_w = znaki_w + ch
        iw = iw + 1
    return znaki_w


def zmien_znaki_5(znaki):
    return zmien_znaki_na_poz(znaki, 2)


def zmien_znaki_6(znaki):
    return zmien_znaki_na_poz(znaki, 3)


def zmien_znaki_7(znaki):
    return zmien_znaki_na_poz(znaki, 4)


def zmien_znaki_8(znaki):
    return zmien_znaki_na_poz(znaki, 1)


def sortuj_wyraz(znaki):
    znaki_list = list(znaki)
    znaki_list.sort()
    return "".join(znaki_list)


def zmien_znaki_9(znaki):
    return sortuj_wyraz(znaki)


def zmien_znaki_10(znaki):
    wyj = ""
    for slowo in znaki.split(" "):
        if not wyj == "":
            wyj = wyj + " "
        wyj = wyj+sortuj_wyraz(slowo)
    return wyj


# jednostkowe testy automatyczne
# https://docs.python.org/3/library/unittest.html#basic-example
class TestCwiczen(unittest.TestCase):

    def test_zmien_znaki_1(self):
        self.assertEqual(zmien_znaki_1(""), "")
        self.assertEqual(zmien_znaki_1("a"), "A")
        self.assertEqual(zmien_znaki_1("aBCd"), "ABCD")

    def test_zmien_znaki_2(self):
        self.assertEqual(zmien_znaki_2(""), "")
        self.assertEqual(zmien_znaki_2("a"), "a")
        self.assertEqual(zmien_znaki_2("aBCd"), "aBCD")

    def test_zmien_znaki_3(self):
        self.assertEqual(zmien_znaki_3(""), "")
        self.assertEqual(zmien_znaki_3("a"), "a")
        self.assertEqual(zmien_znaki_3("aBCd"), "aBCD")

    def test_zmien_znaki_4(self):
        self.assertEqual(zmien_znaki_4(""), "")
        self.assertEqual(zmien_znaki_4("a"), "A")
        self.assertEqual(zmien_znaki_4("ala ma, kota"), "Ala Ma, Kota")

    def test_zmien_znaki_5(self):
        self.assertEqual(zmien_znaki_5(""), "")
        self.assertEqual(zmien_znaki_5("a"), "a")
        self.assertEqual(zmien_znaki_5("ab"), "aB")
        self.assertEqual(zmien_znaki_5("alA ma, kota"), "aLA mA, kOta")

    def test_zmien_znaki_6(self):
        self.assertEqual(zmien_znaki_6(""), "")
        self.assertEqual(zmien_znaki_6("a"), "a")
        self.assertEqual(zmien_znaki_6("abcdef"), "abCdef")
        self.assertEqual(zmien_znaki_6("ala ma, kota"), "alA ma, koTa")

    def test_zmien_znaki_7(self):
        self.assertEqual(zmien_znaki_7(""), "")
        self.assertEqual(zmien_znaki_7("a"), "a")
        self.assertEqual(zmien_znaki_7("abcdef"), "abcDef")
        self.assertEqual(zmien_znaki_7("ala ma, kota"), "ala ma, kotA")

    def test_zmien_znaki_8(self):
        self.assertEqual(zmien_znaki_8(""), "")
        self.assertEqual(zmien_znaki_8("a"), "A")
        self.assertEqual(zmien_znaki_8("ala ma, kota"), "Ala Ma, Kota")

    def test_zmien_znaki_9(self):
        self.assertEqual(zmien_znaki_9(""), "")
        self.assertEqual(zmien_znaki_9("a"), "a")
        self.assertEqual(zmien_znaki_9("ala ma kota"), "  aaaaklmot")

    def test_zmien_znaki_10(self):
        self.assertEqual(zmien_znaki_10(""), "")
        self.assertEqual(zmien_znaki_10("a"), "a")
        self.assertEqual(zmien_znaki_10("ala ma kota"), "aal am akot")
        self.assertEqual(zmien_znaki_10("ala ma kota kota"), "aal am akot akot")
        self.assertEqual(zmien_znaki_10("ala ala ma kota kota"), "aal aal am akot akot")


unittest.main(module=__name__, verbosity=2)
