import unittest


# Zadanie: analiza tekstu
# Zasady:
# - użyj wszystkich poniższych funkcji, zaimplementuj je
# - przed szukaniem samoglosek i wszystkich liter posortuj tekst, nie szukaj tych znaków, gdy nie ma szans ich
#   znaleźć (pętla while)
def zlicz_samogloski(znaki):
    znaki = sorted(znaki)
    samogloski = {"a", "ą", "e", "ę", "i", "o", "ó", "u", "y"}
    wynik = 0
    i = 0
    while i < len(znaki) and znaki[i] <= 'y':
        if znaki[i].lower() in samogloski:
            wynik = wynik + 1
        i += 1
    return wynik


def zlicz_litery(znaki):
    liczba = 0
    for ch in znaki:
        if ch.isalpha():
            liczba = liczba + 1
    return liczba


def zlicz_wyrazy(znaki):
    return len(znaki.split())


def zlicz_zdania(znaki):
    znaki = znaki.strip()
    # https://www.flake8rules.com/rules/E701.html
    if len(znaki) == 0:
        return 0
    return len(znaki.split("."))


def analizuj_tekst(tekst):
    return {
        "zdania": zlicz_zdania(tekst),
        "wyrazy": zlicz_wyrazy(tekst),
        "litery": zlicz_litery(tekst),
        "samogloski": zlicz_samogloski(tekst)
    }


# jednostkowe testy automatyczne
# https://docs.python.org/3/library/unittest.html#basic-example
class TestCwiczen(unittest.TestCase):
    def test_analizuj_tekst(self):
        self.assertEqual(analizuj_tekst(""), {"zdania": 0, "wyrazy": 0, "litery": 0, "samogloski": 0})
        self.assertEqual(analizuj_tekst("          "), {"zdania": 0, "wyrazy": 0, "litery": 0, "samogloski": 0})
        self.assertEqual(analizuj_tekst("Ala   ma   Kota"), {"zdania": 1, "wyrazy": 3, "litery": 9, "samogloski": 5})
        self.assertEqual(analizuj_tekst("Ala ma. Kota"), {"zdania": 2, "wyrazy": 3, "litery": 9, "samogloski": 5})
        self.assertEqual(analizuj_tekst("Alaaa.  ma, Kota"), {"zdania": 2, "wyrazy": 3, "litery": 11, "samogloski": 7})


unittest.main(module=__name__, verbosity=2)
