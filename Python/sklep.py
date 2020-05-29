import unittest
from enum import Enum
from typing import List


# jako: klient sklepu
# chciałbym: przeszukiwać ofertę sklepu
# aby: znaleźć szukany towar po fragmencie nazwy, posortować towary w kolejności: cenie rosnaco i ocenie malejaco
#
# jako: klient sklepu
# chciałbym: znaleziony towar zamiescic w koszyku
# aby: przeglądać to co mam już zgromadzone i na koniec zamówić


class ProstaEncja:
    __id: str
    __nazwa: str
    __opis: str

    def __init__(self, eid: str, nazwa: str, opis: str = ""):
        self.__id = eid
        self.__nazwa = nazwa
        self.__opis = opis

    @property
    def id(self) -> str:
        return self.__id

    @property
    def nazwa(self) -> str:
        return self.__nazwa

    @property
    def opis(self) -> str:
        return self.__opis


class Klient(ProstaEncja):
    pass


class Towar:
    __id: int
    __nazwa: str
    __nazwa_lower: str
    __cena: float
    __ocena: int

    def __init__(self, tid: int, nazwa: str, cena: float, ocena: int):
        self.__id = tid
        self.__nazwa = nazwa
        self.__nazwa_lower = nazwa.lower()
        self.__cena = cena
        self.__ocena = ocena

    def podaj_id(self) -> int:
        return self.__id

    def podaj_nazwe(self) -> str:
        return self.__nazwa

    def podaj_nazwe_lower(self) -> str:
        return self.__nazwa_lower

    def podaj_cene(self) -> float:
        return self.__cena

    def podaj_ocene(self) -> int:
        return self.__ocena


class KolejnoscSortowania(Enum):
    CENA_ROSNACO = 1
    OCENA_MALEJACO = 2


class Oferta:
    __lista_towarow: List[Towar]

    def __init__(self):
        self.__lista_towarow = []

    @staticmethod
    def __sortuj(towary: List[Towar], kolejnosc: KolejnoscSortowania) -> List[Towar]:
        if kolejnosc == KolejnoscSortowania.OCENA_MALEJACO:
            towary.sort(key=lambda towar: towar.podaj_ocene(), reverse=True)
        elif kolejnosc == KolejnoscSortowania.CENA_ROSNACO:
            towary.sort(key=lambda towar: towar.podaj_cene(), reverse=False)
        return towary

    def szukaj_po_nazwie(self, nazwa: str, kolejnosc: KolejnoscSortowania) -> List[Towar]:
        res: List[Towar] = []
        nazwa = nazwa.lower()
        for t in self.__lista_towarow:
            if t.podaj_nazwe_lower().find(nazwa) >= 0:
                res.append(t)
        return Oferta.__sortuj(res, kolejnosc)

    def dodaj_towar(self, towar: Towar):
        self.__lista_towarow.append(towar)

    def podaj_towar_po_id(self, tid) -> Towar:
        return self.__lista_towarow[tid]


class TowarZamowiony:
    __ilosc: int
    __towar: Towar

    def __init__(self, towar: Towar, ilosc: int):
        self.__ilosc = ilosc
        self.__towar = towar

    # https://stackoverflow.com/questions/2627002/whats-the-pythonic-way-to-use-getters-and-setters
    @property
    def ilosc(self) -> int:
        return self.__ilosc

    @ilosc.setter
    def ilosc(self, value):
        self.__ilosc = value

    @property
    def towar(self) -> Towar:
        return self.__towar


class Koszyk:

    def __init__(self):
        self.__lista: List[TowarZamowiony] = []

    def dodaj_towar(self, towar: Towar, ilosc: int):
        for tz in self.__lista:
            if towar.podaj_id() == tz.towar.podaj_id():
                tz.ilosc += ilosc
                return
        self.__lista.append(TowarZamowiony(towar, ilosc))

    def podaj_zawartosc(self) -> List[TowarZamowiony]:
        return self.__lista


class Platnosc(ProstaEncja):
    pass


class Dostawa(ProstaEncja):
    pass


class Zamowienie:
    __klient: Klient
    __lista_towarow: List[TowarZamowiony]
    __platnosc: Platnosc
    __dostawa: Dostawa

    def __init__(self, klient: Klient, koszyk: Koszyk, platnosc: Platnosc, dostawa: Dostawa):
        self.__klient = klient
        self.__lista_towarow = koszyk.podaj_zawartosc().copy()
        self.__platnosc = platnosc
        self.__dostawa = dostawa

    def podaj_wartosc(self) -> float:
        return sum(map(lambda tz: tz.ilosc * tz.towar.podaj_cene(), self.__lista_towarow))


class ListaZamowien:

    def __init__(self):
        self.__lista: List[Zamowienie] = []

    def zloz_zamowienie(self, zamowienie: Zamowienie) -> str:
        self.__lista.append(zamowienie)
        return str(len(self.__lista) - 1)

    def podaj_zam_po_nr(self, nr: str) -> Zamowienie:
        return self.__lista[int(nr)]


# jednostkowe testy automatyczne
# https://docs.python.org/3/library/unittest.html#basic-example
class TestCwiczen(unittest.TestCase):
    o1: Oferta
    o2: Oferta

    def setUp(self):
        # oferta 1
        self.o1 = Oferta()
        self.o1.dodaj_towar(Towar(0, "TV", 300, 1))
        self.o1.dodaj_towar(Towar(1, "Monitor 1", 300, 1))
        self.o1.dodaj_towar(Towar(2, "Monitor 2", 501, 9))

        # oferta 2
        self.o2 = Oferta()
        self.o2.dodaj_towar(Towar(0, "Placki", 200, 1))
        self.o2.dodaj_towar(Towar(1, "Ziemniaki", 100, 1))
        self.o2.dodaj_towar(Towar(2, "Buraki", 501, 9))

    # jako: klient sklepu
    # chciałbym: przeszukiwać ofertę sklepu
    # aby: znaleźć szukany towar po fragmencie nazwy, posortować towary w kolejności: cenie rosnaco i ocenie malejaco

    def test_szukania_najlepszej_oceny(self):
        # given: oferta o1
        o = self.o1
        # when: szukamy monitora o nazwie zawierajacej fragment "Monitor" w kolejności najlepszej oceny
        towary = o.szukaj_po_nazwie("Monitor", KolejnoscSortowania.OCENA_MALEJACO)
        # then: otrzymujemy listę posortowaną [Monitor 2, Monitor 1]
        self.assertEqual(len(towary), 2)
        self.assertEqual(towary[0].podaj_nazwe(), "Monitor 2")
        self.assertEqual(towary[0].podaj_ocene(), 9)

    def test_szukania_najnizszej_ceny(self):
        # given: oferta o1
        o = self.o1
        # when: szukamy monitora o nazwie zawierajacej fragment "Monitor" w kolejności najlepszej ceny
        towary = o.szukaj_po_nazwie("Monitor", KolejnoscSortowania.CENA_ROSNACO)
        # then: otrzymujemy listę posortowaną [Monitor 1, Monitor 2]
        self.assertEqual(len(towary), 2)
        self.assertEqual(towary[0].podaj_nazwe(), "Monitor 1")
        self.assertEqual(towary[0].podaj_cene(), 300)

    # jako: klient sklepu
    # chciałbym: znaleziony towar zamiescic w koszyku
    # aby: przeglądać to co mam już zgromadzone i na koniec zamówić
    def sprawdz_2towary_w_koszyku(self, lista, idx: int):
        twk: TowarZamowiony = lista[idx]
        if twk.towar.podaj_id() == 0:
            self.assertEqual(twk.ilosc, 1, "Towar w koszyku na poz " + str(idx) + " ma złą ilosc")
        elif twk.towar.podaj_id() == 1:
            self.assertEqual(twk.ilosc, 5, "Towar w koszyku na poz " + str(idx) + " ma złą ilosc")

    def test_dodawania_do_koszyka(self):
        # given: oferta o2 i pusty koszyk
        o: Oferta = self.o2
        k: Koszyk = Koszyk()

        # when: dodamy do koszyka 2 towary
        k.dodaj_towar(o.podaj_towar_po_id(0), 1)
        t1: Towar = o.podaj_towar_po_id(1)
        k.dodaj_towar(t1, 3)
        k.dodaj_towar(t1, 2)

        # then: mozemy je wyswietlic
        lista: List[TowarZamowiony] = k.podaj_zawartosc()
        self.assertEqual(len(lista), 2, "Zla zawartosc koszyka")
        self.sprawdz_2towary_w_koszyku(lista, 0)
        self.sprawdz_2towary_w_koszyku(lista, 1)

    def test_sladania_zamowienia(self):
        # given: oferta o2 i pusty koszyk
        o: Oferta = self.o2
        k: Koszyk = Koszyk()
        lz: ListaZamowien = ListaZamowien()

        # when: dodamy do koszyka 2 towary
        t0: Towar = o.podaj_towar_po_id(0)
        k.dodaj_towar(t0, 1)
        t1: Towar = o.podaj_towar_po_id(1)
        k.dodaj_towar(t1, 3)
        k.dodaj_towar(t1, 2)

        # then: mozemy zlozyc zamowienie
        z: Zamowienie = Zamowienie(
            Klient("K1", "Jan Kowalski"),
            k,
            Platnosc("G", "Gotówka"),
            Dostawa("K", "Kurier DHL")
        )
        nr_zam: str = lz.zloz_zamowienie(z)
        self.assertTrue(len(nr_zam) > 0, "Nr zamowienia jest zły!")
        zam_z_listy: Zamowienie = lz.podaj_zam_po_nr(nr_zam)
        self.assertEqual(zam_z_listy.podaj_wartosc(), (1 * t0.podaj_cene() + 5 * t1.podaj_cene()),
                         "Zla wartosc zamowienia!")


unittest.main(module=__name__, verbosity=2)
