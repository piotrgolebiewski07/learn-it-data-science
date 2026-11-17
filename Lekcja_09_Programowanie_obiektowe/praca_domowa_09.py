import math
import statistics
from datetime import datetime
from math import isnan # zadanie 18

####################################
print("---", "Zadanie 1", "---")


####################################


class Produkt():
    def __init__(self, nazwa, cena, ilosc_w_magazynie: int):
        self.nazwa = nazwa
        self.cena = cena
        self.ilosc_w_magazynie = ilosc_w_magazynie

    def pokaz_info(self):
        print(f"Nazwa produktu: {self.nazwa}, cena: {self.cena}, ilość: {self.ilosc_w_magazynie}")

    def sprzedaj(self, ilosc):
        self.ilosc_w_magazynie = self.ilosc_w_magazynie - ilosc

    def dostawa(self, ilosc):
        self.ilosc_w_magazynie = self.ilosc_w_magazynie + ilosc


produkt1 = Produkt("Stół", 600, 4)
produkt2 = Produkt("Krzesło", 200, 12)
produkt3 = Produkt("Łóżko", 1100, 3)

produkt1.pokaz_info()
produkt1.sprzedaj(2)
produkt1.dostawa(17)
produkt1.pokaz_info()

produkt2.pokaz_info()
produkt2.sprzedaj(1)
produkt2.dostawa(10)
produkt2.pokaz_info()

produkt3.pokaz_info()
produkt3.sprzedaj(2)
produkt3.dostawa(1)
produkt3.pokaz_info()

####################################
print("---", "Zadanie 2", "---")


####################################


class Kalkulator():

    def dodaj(self, a, b):
        """Oblicza sumę dwóch liczb"""
        return a + b

    def odejmij(self, a, b):
        """Oblicza różnicę dwóch liczb"""
        return a - b

    def pomnoz(self, a, b):
        """Oblicza iloczyn dwóch liczb"""
        return a * b

    def podziel(self, a, b):
        """Oblicza iloraz dwóch liczb"""
        return a / b


kalkulator = Kalkulator()
print(f"Wynik dodawania liczb: {kalkulator.dodaj(2, 5)}")
print(f"Wynik odejmowania liczb: {kalkulator.odejmij(15, 30)}")
print(f"Wynik mnożenia liczb: {kalkulator.pomnoz(64, 4)}")
print(f"Wynik dzielenia liczb: {kalkulator.podziel(125, 5)}")

####################################
print("---", "Zadanie 3", "---")


####################################

class BankAccount():

    def __init__(self, wlasciciel, saldo):
        self.wlasciciel = wlasciciel
        self.saldo = saldo

    def wplac(self, kwota):
        self.saldo += kwota
        return self.saldo

    def wyplac(self, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
            return self.saldo
        else:
            print(f"Brak środków: Na koncie pozostało {self.saldo}zł")
            return self.saldo

    def pokaz_saldo(self):
        return self.saldo


konto1 = BankAccount("Tomek", 500)
konto2 = BankAccount("Marta", 2000)

print(f"Saldo konta Tomka:")
print(konto1.pokaz_saldo())
print(konto1.wplac(200))
print(konto1.wyplac(800))
print(konto1.wyplac(300))

print(f"\nSaldo konta Marty:")
print(konto2.pokaz_saldo())
print(konto2.wplac(200))
print(konto2.wyplac(800))

####################################
print("---", "Zadanie 4", "---")


####################################


class Ksiazka():

    def __init__(self, tytul, autor, rok_wydania, liczba_stron):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania
        self.liczba_stron = liczba_stron

    def __str__(self):
        return (
            f"Tytuł: {self.tytul}\n"
            f"Autor: {self.autor}\n"
            f"Rok wydania: {self.rok_wydania}\n"
            f"Liczba stron: {self.liczba_stron}"
        )


ksiazki = [
    Ksiazka("Hobbit, czyli tam i z powrotem", "J.R.R. Tolkien", 1937, 310),
    Ksiazka("Władca Pierścieni: Drużyna Pierścienia", "J.R.R. Tolkien", 1954, 423),
    Ksiazka("Władca Pierścieni: Dwie wieże", "J.R.R. Tolkien", 1954, 352),
    Ksiazka("Władca Pierścieni: Powrót króla", "J.R.R. Tolkien", 1955, 416),
    Ksiazka("Silmarillion", "J.R.R. Tolkien", 1977, 365),
]

for ksiazka in ksiazki:
    print(ksiazka)
    print()

####################################
print("---", "Zadanie 5", "---")


####################################


class Student():

    def __init__(self, imie, numer_indeksu, oceny):
        self.imie = imie
        self.numer_indeksu = numer_indeksu
        self.oceny = oceny

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)
        return self.oceny

    def srednia(self):
        return sum(self.oceny) / len(self.oceny)

    def __str__(self):
        return (f"Student {self.imie} o numerze indeksu: {self.numer_indeksu} ma oceny: {self.oceny}")


student1 = Student("Piotr", 1, [4, 5])
student2 = Student("Anna", 2, [3, 4, 2, 5])
student3 = Student("Jan", 3, [6])

student1.dodaj_ocene(4)
student2.dodaj_ocene(5)
student3.dodaj_ocene(3)

for student in [student1, student2, student3]:
    print(student)
    print(f"Średnia ocen: {student.srednia():.2f}\n")

####################################
print("---", "Zadanie 6", "---")


####################################


class Pojazd():

    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok

    def pokaz_info(self):
        print(f"Marka samochodu: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Rok: {self.rok}")


class Samochod(Pojazd):

    def __init__(self, marka, model, rok, liczba_drzwi):
        super().__init__(marka, model, rok)
        self.liczba_drzwi = liczba_drzwi

    def pokaz_info(self):
        super().pokaz_info()
        print(f"Liczba drzwi: {self.liczba_drzwi}")


samochod = Samochod("Skoda", "Octavia", 1990, 5)
samochod.pokaz_info()

####################################
print("---", "Zadanie 7", "---")


####################################


class Pracownik():

    def __init__(self, imie, stanowisko, pensja):
        self.imie = imie
        self.stanowisko = stanowisko
        self.pensja = pensja

    def podwyzka(self, procent):
        self.procent = procent
        self.pensja_przed_podwyzka = self.pensja
        self.pensja = self.pensja * (1 + self.procent / 100)

    def __str__(self):
        return f"Pracownikowi {self.imie} zostało zwiększone wynagrodzenie z {self.pensja_przed_podwyzka} do {self.pensja} czyli o {self.procent}%"


pracownik1 = Pracownik("Andrzej", "dyrektor", 14000)
pracownik1.podwyzka(50)
print(pracownik1)

pracownik2 = Pracownik("Marek", "kierownik", 10000)
pracownik2.podwyzka(35)
print(pracownik2)

pracownik3 = Pracownik("Bartek", "programista junio", 5000)
pracownik3.podwyzka(20)
print(pracownik3)

####################################
print("---", "Zadanie 8", "---")


####################################


class Zadanie():

    def __init__(self, opis, status="do zrobienia"):
        self.opis = opis
        self.status = status

    def oznacz_jako_zrobione(self):
        self.status = "zrobione"

    def __str__(self):
        return f"Zadanie '{self.opis}' ma status '{self.status}'"


zadania = [
    Zadanie("Powtórzyć podstawy klas"),
    Zadanie("Napisać program w Pythonie"),
    Zadanie("Przygotować obiad"),
    Zadanie("Posprzątać biurko"),
    Zadanie("Przeczytać rozdział książki")
]

zadania[0].oznacz_jako_zrobione()
zadania[4].oznacz_jako_zrobione()

for zadanie in zadania:
    print(zadanie)

####################################
print("---", "Zadanie 9", "---")


####################################


class FiltrowanieDodatnich():
    def wykonaj(self, dane):
        return [i for i in dane if i >= 0]


class Zaokraglenie():
    def wykonaj(self, dane):
        return [round(i) for i in dane]


class Skalowanie():
    def __init__(self, liczba):
        self.liczba = liczba

    def wykonaj(self, dane):
        return [i * self.liczba for i in dane]


class Sumowanie():
    def wykonaj(self, dane):
        return sum(dane)


class Pipeline:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.kroki = []

    def dodaj_krok(self, krok):
        self.kroki.append(krok)

    def uruchom(self, dane):
        wynik = dane
        for krok in self.kroki:
            wynik = krok.wykonaj(wynik)
        return (wynik)


dane = [1.7, -3.2, 5.8, -1.1, 8.3, 2.4]

pipeline = Pipeline("Przetwarzanie")
pipeline.dodaj_krok(FiltrowanieDodatnich())
pipeline.dodaj_krok(Zaokraglenie())
pipeline.dodaj_krok(Skalowanie(5))
pipeline.dodaj_krok(Sumowanie())

wynik = pipeline.uruchom(dane)
print(wynik)

####################################
print("---", "Zadanie 10", "---")


####################################


class Produkt():
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena


class Zamowienie():
    def __init__(self):
        self.lista_produktow = []

    def dodaj_produkt(self, produkt, ilosc):
        znaleziono = False

        for i in self.lista_produktow:
            if i["produkt"].nazwa == produkt.nazwa:
                i["ilość"] += ilosc
                znaleziono = True
        if not znaleziono:
            self.lista_produktow.append({
                "produkt": produkt,
                "ilość": ilosc
            })

    def laczna_wartosc(self):
        suma = 0
        for i in self.lista_produktow:
            suma += i['produkt'].cena * i['ilość']
        return suma

    def pokaza_zamowienie(self):
        print("--- ZAMÓWIENIE ---\n")
        for i in self.lista_produktow:
            print(f"{i['produkt'].nazwa}\n"
                  f"Ilość: {i['ilość']}\n"
                  f"Cena za sztukę: {i['produkt'].cena} zł\n"
                  f"Wartość: {i['ilość'] * i['produkt'].cena} zł\n"
                  )
        print(f"Łączna wartośc zamówienia: {self.laczna_wartosc()} zł")


produkt1 = Produkt("Laptop", 3500)
produkt2 = Produkt("Monitor", 1200)
produkt3 = Produkt("Klawiatura", 250)
produkt4 = Produkt("Mysz", 100)
produkt5 = Produkt("Słuchawki", 300)

zamowienie = Zamowienie()
zamowienie.dodaj_produkt(produkt1, 3)
zamowienie.dodaj_produkt(produkt2, 2)
zamowienie.dodaj_produkt(produkt3, 1)
zamowienie.dodaj_produkt(produkt4, 2)
zamowienie.dodaj_produkt(produkt5, 1)
zamowienie.dodaj_produkt(produkt1, 2)

zamowienie.pokaza_zamowienie()

####################################
print("---", "Zadanie 11", "---")


####################################


class Uczen():
    def __init__(self, imie, oceny=[]):
        self.imie = imie
        self.oceny = oceny


class Klasa():
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.uczniowie = []

    def dodaj_ucznia(self, uczen):
        znaleziono = False

        for i in self.uczniowie:
            if uczen.imie == i.imie:
                znaleziono = True
                print("Uczeń już istnieje.")

        if not znaleziono:
            self.uczniowie.append(uczen)

    def srednia_klasy(self):
        suma = 0
        ilosc_ocen = 0

        for i in self.uczniowie:
            suma += sum(i.oceny)
            ilosc_ocen += len(i.oceny)

        if ilosc_ocen == 0:
            print("Brak ocen")
            return None

        return suma / ilosc_ocen

    def najlepszy_uczen(self):

        if self.uczniowie == []:
            return None

        najlepszy = self.uczniowie[0]
        srednia_najlepszego = None

        for i in self.uczniowie:
            suma = sum(i.oceny)
            ilosc_ocen = len(i.oceny)

            if ilosc_ocen == 0:
                continue
            srednia = suma / ilosc_ocen

            if srednia_najlepszego is None or srednia_najlepszego < srednia:
                srednia_najlepszego = srednia
                najlepszy = i

        return najlepszy, srednia_najlepszego


uczen1 = Uczen("Paweł", [3, 5, 2, 4])
uczen2 = Uczen("Piotr", [4, 5, 6])
uczen3 = Uczen("Karolina", [5, 6, 3, 5])
uczen4 = Uczen("Adam", [3, 4, 4, 5])
uczen5 = Uczen("Laura", [6, 6, 5, 6])

klasa1 = Klasa("5A")
klasa1.dodaj_ucznia(uczen1)
klasa1.dodaj_ucznia(uczen2)
klasa1.dodaj_ucznia(uczen3)
klasa1.dodaj_ucznia(uczen4)
klasa1.dodaj_ucznia(uczen5)

print(f"Średnia klasy: {klasa1.srednia_klasy():.2f}")
najlepszy, srednia = klasa1.najlepszy_uczen()

print(f"Najlepszy uczeń: {najlepszy.imie}")
print(f"Jego średnia: {srednia:.2f}")

####################################
print("---", "Zadanie 12", "---")


####################################


class Figura():
    def pole(self):
        return f"Obliczamy pole:"


class Prostokat(Figura):
    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc

    def pole(self):
        return self.szerokosc * self.wysokosc


class Kolo(Figura):
    def __init__(self, promien):
        self.promien = promien

    def pole(self):
        return 3.14 * self.promien * self.promien


figury = [
    Prostokat(5, 4),
    Kolo(3),
    Prostokat(2, 6),
    Kolo(5)
]

pole = 0
for figura in figury:
    pole += figura.pole()

print(pole)

####################################
print("---", "Zadanie 13", "---")


####################################


class Ksiazka:
    def __init__(self, tytul, autor, dostepna=True):
        self.tytul = tytul
        self.autor = autor
        self.dostepna = dostepna


class Uzytkownik:
    def __init__(self, imie):
        self.imie = imie
        self.wypozyczone_ksiazki = []


class Biblioteka:
    def __init__(self):
        self.ksiazki = []
        self.uzytkownicy = []

    def dodaj_ksiazke(self, ksiazka):
        self.ksiazki.append(ksiazka)

    def zarejestruj_uzytkownika(self, uzytkownik):
        self.uzytkownicy.append(uzytkownik)

    def wypozycz(self, uzytkownik, ksiazka):
        if (ksiazka in self.ksiazki) and ksiazka.dostepna and (uzytkownik in self.uzytkownicy):
            uzytkownik.wypozyczone_ksiazki.append(ksiazka)
            ksiazka.dostepna = False
        else:
            print("Książka niedostępna")

    def zwroc(self, uzytkownik, ksiazka):
        if ksiazka in uzytkownik.wypozyczone_ksiazki:
            uzytkownik.wypozyczone_ksiazki.remove(ksiazka)
            ksiazka.dostepna = True

    def raport(self):
        suma_wypozyczonych = 0
        for i in self.uzytkownicy:
            suma_wypozyczonych += len(i.wypozyczone_ksiazki)

        print(f"=== Raport ===\n"
              f"Liczba użytkowników: {len(self.uzytkownicy)}\n"
              f"Liczba książek: {len(self.ksiazki)}\n"
              f"Książki wypożyczone: {suma_wypozyczonych}\n"
              f"Ksiązki dostępne: {len(self.ksiazki) - suma_wypozyczonych}\n"
              )

        print("=== Wypożyczenia użytkowników ===")

        for i in self.uzytkownicy:
            print(f"\n{i.imie}")

            for ksiazka in i.wypozyczone_ksiazki:
                print(f"- {ksiazka.tytul} - {ksiazka.autor}")


ksiazka1 = Ksiazka("Hobbit", "J.R.R. Tolkien")
ksiazka2 = Ksiazka("Władca Pierścieni", "J.R.R. Tolkien")
ksiazka3 = Ksiazka("Silmarillion", "J.R.R. Tolkien")
ksiazka4 = Ksiazka("Wiedźmin: Ostatnie życzenie", "Andrzej Sapkowski")
ksiazka5 = Ksiazka("Wiedźmin: Miecz przeznaczenia", "Andrzej Sapkowski")
ksiazka6 = Ksiazka("Gra o tron", "George R.R. Martin")
ksiazka7 = Ksiazka("Starcie królów", "George R.R. Martin")
ksiazka8 = Ksiazka("Z mgły zrodzony", "Brandon Sanderson")
ksiazka9 = Ksiazka("Droga królów", "Brandon Sanderson")
ksiazka10 = Ksiazka("Kolor magii", "Terry Pratchett")

uzytkownik1 = Uzytkownik("Piotr")
uzytkownik2 = Uzytkownik("Maciej")
uzytkownik3 = Uzytkownik("Szymon")

biblioteka = Biblioteka()

ksiazki = [ksiazka1, ksiazka2, ksiazka3, ksiazka4, ksiazka5, ksiazka6, ksiazka7, ksiazka8, ksiazka9, ksiazka10]
for i in ksiazki:
    biblioteka.dodaj_ksiazke(i)

biblioteka.zarejestruj_uzytkownika(uzytkownik1)
biblioteka.zarejestruj_uzytkownika(uzytkownik2)
biblioteka.zarejestruj_uzytkownika(uzytkownik3)

biblioteka.wypozycz(uzytkownik1, ksiazka1)
biblioteka.wypozycz(uzytkownik2, ksiazka2)
biblioteka.wypozycz(uzytkownik2, ksiazka3)
biblioteka.wypozycz(uzytkownik2, ksiazka4)
biblioteka.zwroc(uzytkownik2, ksiazka4)
biblioteka.wypozycz(uzytkownik3, ksiazka9)
biblioteka.wypozycz(uzytkownik3, ksiazka10)
biblioteka.wypozycz(uzytkownik2, ksiazka10)
biblioteka.wypozycz(uzytkownik1, ksiazka1)
biblioteka.wypozycz(uzytkownik2, ksiazka1)

biblioteka.raport()

####################################
print("---", "Zadanie 14", "---")


####################################


class LogTransformer:
    def __init__(self):
        self.nazwa = "Transformacja logarytmiczna"

    def transform(self, dane):
        wynik = []
        for i in dane:
            wynik.append(math.log(i + 1, 10))
        return wynik


class OutlierRemover:
    def __init__(self):
        self.nazwa = "Usuwanie wartości odstających"

    def transform(self, dane):
        srednia = statistics.mean(dane)
        odchylenie = statistics.pstdev(dane)
        wynik = []

        for i in dane:
            if abs(srednia - i) <= odchylenie * 3:
                wynik.append(i)
        return wynik


class BinningTransformer:
    def __init__(self):
        self.nazwa = "Podział na przedziały"

    def transform(self, dane):
        minimum = min(dane)
        maksimum = max(dane)
        szerokosc = (maksimum - minimum) / 3

        przedzial_1 = []
        przedzial_2 = []
        przedzial_3 = []

        for i in dane:
            if i < (minimum + szerokosc):
                przedzial_1.append(i)
            elif i < (minimum + 2 * szerokosc):
                przedzial_2.append(i)
            else:
                przedzial_3.append(i)

        return przedzial_1, przedzial_2, przedzial_3


class Pipeline:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.kroki = []

    def dodaj_krok(self, krok):
        self.kroki.append(krok)

    def uruchom(self, dane):
        print(f"=== Pipeline: {self.nazwa} ===")
        wynik = dane

        for krok in self.kroki:
            print(f"\nWykonuję: {krok.nazwa}")
            wynik = krok.transform(wynik)
            print(wynik)

        print(f"\nWynik końcowy: {wynik}")
        return wynik


# Tworzenie pipeline'a z komponentów
pipeline = Pipeline("Przetwarzanie danych sprzedaży")
pipeline.dodaj_krok(LogTransformer())
pipeline.dodaj_krok(OutlierRemover())
pipeline.dodaj_krok(BinningTransformer())

# Uruchomienie pipeline'a
data = [1, 5, 10, 100, 2, 3, 8, 200, 4, 6]
wynik = pipeline.uruchom(data)

####################################
print("---", "Zadanie 15", "---")
####################################


class Akcja:
    def __init__(self, nazwa, cena_kupna, cena_aktualna):
        self.nazwa = nazwa
        self.cena_kupna = cena_kupna
        self.cena_aktualna = cena_aktualna


class Portfel:
    def __init__(self, kapital_poczatkowy):
        self.akcje = {}
        self.kapital_poczatkowy = kapital_poczatkowy
        self.gotowka = kapital_poczatkowy

    def kup_akcje(self, akcja, ilosc):
        if self.gotowka >= (akcja.cena_kupna * ilosc):
            if akcja not in self.akcje.keys():
                self.akcje[akcja] = ilosc
            else:
                self.akcje[akcja] += ilosc
            self.gotowka -= akcja.cena_kupna * ilosc
        else:
            print("Brak gotówki")
        return self.akcje

    def sprzedaj_akcje(self, akcja, ilosc):
        if akcja in self.akcje.keys():
            if self.akcje[akcja] >= ilosc > 0:
                self.gotowka += akcja.cena_aktualna * ilosc
                self.akcje[akcja] -= ilosc
                if self.akcje[akcja] == 0:
                    del self.akcje[akcja]
            else:
                print("Nie możesz sprzedać - masz za mało akcji")
        else:
            print("Brak akcji w portfelu")
        return self.akcje

    def aktualizuj_ceny(self, slownik_cen):
        for klucz, wartosc in slownik_cen.items():
            for akcja in self.akcje.keys():
                if akcja.nazwa == klucz:
                    akcja.cena_aktualna = wartosc

    def wartosc_portfela(self):
        wartosc_akcji = 0

        for akcja, ilosc in self.akcje.items():
            print(f"\n====== {akcja.nazwa} ======")
            print(f"Ilość akcji:", ilosc)

            wartosc_akcji += ilosc * akcja.cena_aktualna
            print(f"Wartość akcji: {ilosc * akcja.cena_aktualna}")


        print(f"\nGotówka: {self.gotowka}")
        print(f"Akcje: {wartosc_akcji}")
        wartosc = wartosc_akcji + self.gotowka
        print(f"Łączna wartość: {wartosc}")

        return wartosc

    def zysk_strata(self):
        return self.wartosc_portfela() - self.kapital_poczatkowy


akcja1 = Akcja("CD Projekt", 150.00, 140.00)
akcja2 = Akcja("PKO BP", 60.00, 55.00)
portfel = Portfel(2000)

portfel.kup_akcje(akcja1, 3)
portfel.kup_akcje(akcja2, 5)
portfel.kup_akcje(akcja1, 4)
portfel.sprzedaj_akcje(akcja1, 2)
portfel.sprzedaj_akcje(akcja1, 2)
portfel.aktualizuj_ceny({"CD Projekt": 1})
portfel.wartosc_portfela()
print(f"\nZysk/strata: {portfel.zysk_strata()}")

####################################
print("---", "Zadanie 16", "---")
####################################


class Zwierze():
    def __init__(self, nazwa, wiek):
        self.nazwa = nazwa
        self.wiek = wiek

    def pokaz_info(self):
        print(self.nazwa, self.wiek)


class Ssak(Zwierze):
    def __init__(self, nazwa, wiek, typ_futra):
        super().__init__(nazwa, wiek)
        self.typ_futra = typ_futra

    def pokaz_info(self):
        super().pokaz_info()
        print(self.typ_futra)


class Pies(Ssak):
    def __init__(self, nazwa, wiek, typ_futra, rasa):
        super().__init__(nazwa, wiek, typ_futra)
        self.rasa = rasa

    def pokaz_info(self):
        super().pokaz_info()
        print(self.rasa)


pies = Pies("Rafi", 5, "sierść", "Cavalier")
pies.pokaz_info()

####################################
print("---", "Zadanie 17", "---")
####################################


class Pokoj:
    def __init__(self, numer, typ, cena_za_noc, zajety=False):
        self.numer = numer
        self.typ = typ
        self.cena = cena_za_noc
        self.zajety = zajety


class Rezerwacja:
    def __init__(self, pokoj, gosc, data_od, data_do):
        self.pokoj = pokoj
        self.gosc = gosc
        self.data_od = data_od
        self.data_do = data_do


class Hotel:
    def __init__(self):
        self.pokoje = []
        self.rezerwacje = []

    def dodaj_pokoj(self, pokoj):
        self.pokoje.append(pokoj)

    def rezerwuj(self, numer_pokoju, gosc, data_od, data_do):
        for pokoj in self.pokoje:
            if pokoj.numer == numer_pokoju and not pokoj.zajety:
                rezerwacja = Rezerwacja(pokoj, gosc, data_od, data_do)
                self.rezerwacje.append(rezerwacja)
                pokoj.zajety = True

    def wolne_pokoje(self):
        wynik = []
        for pokoj in self.pokoje:
            if not pokoj.zajety:
                wynik.append(pokoj)
        return wynik

    def przychod(self):
        wynik = 0
        for rezerwacja in self.rezerwacje:
            data_od = datetime.strptime(rezerwacja.data_od, "%d.%m.%Y")
            data_do = datetime.strptime(rezerwacja.data_do, "%d.%m.%Y")

            roznica = data_do - data_od
            wynik += roznica.days * rezerwacja.pokoj.cena
        return wynik


pokoje = [
    Pokoj(1, "jednoosobowy", 300),
    Pokoj(2, "jednoosobowy", 320),
    Pokoj(3, "dwuosobowy", 450),
    Pokoj(4, "dwuosobowy", 500),
    Pokoj(5, "trzyosobowy", 600),
    Pokoj(6, "trzyosobowy", 650),
    Pokoj(7, "apartament", 900),
    Pokoj(8, "apartament", 1000),
    Pokoj(9, "jednoosobowy", 280),
    Pokoj(10, "dwuosobowy", 480)
]

hotel = Hotel()

for pokoj in pokoje:
    hotel.dodaj_pokoj(pokoj)

hotel.rezerwuj(1, "Piotr", "10.11.2026", "14.11.2026")
hotel.rezerwuj(3, "Adam", "12.11.2026", "15.11.2026")
hotel.rezerwuj(5, "Anna", "15.11.2026", "20.11.2026")
hotel.rezerwuj(7, "Kasia", "18.11.2026", "22.11.2026")
hotel.rezerwuj(10, "Marek", "20.11.2026", "23.11.2026")

print("Liczba pokoi:", len(hotel.pokoje))
print("Liczba rezerwacji:", len(hotel.rezerwacje))

print("\nWolne pokoje:")
for pokoj in hotel.wolne_pokoje():
    print(pokoj.numer, pokoj.typ, pokoj.cena)

print("\nPrzychód hotelu:", hotel.przychod(), "zł")

####################################
print("---", "Zadanie 18", "---")
####################################


class ValidatorZakresu:
    def __init__(self, minimum, maksimum):
        self.minimum = minimum
        self.maksimum = maksimum

    def wykonaj(self, dane):
        for liczba in dane:
            if isinstance(liczba, (int, float)):
                if not (self.minimum <= liczba <= self.maksimum):
                    komunikat = "Co najmniej jedna liczba jest spoza zakresu"
                    return False, komunikat
        return True, "Wszystko ok"


class ValidatorTypu:
    def __init__(self, typ):
        self.typ = typ

    def wykonaj(self, dane):
        for liczba in dane:
            if not type(liczba) is self.typ:
                komunikat = "Co najmniej jedna liczba jest innego typu"
                return False,  komunikat
        return True, "Wszystko ok"


class ValidatorBrakow:
    def wykonaj(self, dane):
        for liczba in dane:
            if liczba is None or isnan(liczba):
                komunikat = "Co najmniej jedna liczba jest None lub NaN"
                return False, komunikat
        return True, "Wszystko ok"


class Pipeline:
    def __init__(self):
        self.kroki = []

    def dodaj_krok(self, krok):
        self.kroki.append(krok)

    def uruchom(self, dane):
        lista = []
        for i in self.kroki:
            wynik = i.wykonaj(dane)
            lista.append(wynik)
        return lista


pipeline = Pipeline()
pipeline.dodaj_krok(ValidatorZakresu(1, 4))
pipeline.dodaj_krok(ValidatorTypu(int))
pipeline.dodaj_krok(ValidatorBrakow())

wynik = pipeline.uruchom([1, 2, 3, None])
print(wynik)

####################################
print("---", "Zadanie 19", "---")
####################################


class Postac:
    def __init__(self, imie, hp, atak, obrona, mnoznik_leczenia=1):
        self.imie = imie
        self.hp = hp
        self.atak = atak
        self.obrona = obrona
        self.max_hp = hp
        self.mnoznik_leczenia = mnoznik_leczenia

    def atakuj(self, cel):
        obrazenia = self.atak - cel.obrona
        if obrazenia > 0:
            if obrazenia >= cel.hp:
                cel.hp = 0
            else:
                cel.hp -= obrazenia

    def leczenie(self, punkty):
        if self.hp > 0 and (self.hp + punkty * self.mnoznik_leczenia <= self.max_hp):
            self.hp += punkty * self.mnoznik_leczenia
        elif self.hp > 0 and (self.hp + punkty * self.mnoznik_leczenia > self.max_hp):
            self.hp = self.max_hp


class Wojownik(Postac):
    def __init__(self, imie, hp, atak, obrona, mnoznik_leczenia=0.8):
        atak = 1.5 * atak
        super().__init__(imie, hp, atak, obrona, mnoznik_leczenia)


class Mag(Postac):
    def __init__(self, imie, hp, atak, obrona, mnoznik_leczenia=1.5):
        obrona = 1.3 * obrona
        super().__init__(imie, hp, atak, obrona, mnoznik_leczenia)


class Lucznik(Postac):
    def __init__(self, imie, hp, atak, obrona,mnoznik_leczenia=1.15):
        atak = 1.1 * atak
        obrona = 1.1 * obrona
        super().__init__(imie, hp, atak, obrona, mnoznik_leczenia)


wojownik = Wojownik("Aragorn", 100, 30, 15)
mag = Mag("Gandalf", 80, 20, 5)
lucznik = Lucznik("Legolas", 90, 20, 10)

# Runda 1
wojownik.atakuj(mag)
print(f"Aragorn atakuje Gandalfa. HP Gandalfa: {mag.hp}")

mag.atakuj(lucznik)
print(f"Gandalf atakuje Legolasa. HP Legolasa: {lucznik.hp}")

lucznik.atakuj(wojownik)
print(f"Legolas atakuje Aragorna. HP Aragorna: {wojownik.hp}")

# Runda 2
wojownik.atakuj(mag)
print(f"Aragorn atakuje Gandalfa. HP Gandalfa: {mag.hp}")

mag.leczenie(20)
print(f"Gandalf leczy się. HP Gandalfa: {mag.hp}")

lucznik.atakuj(wojownik)
print(f"Legolas atakuje Aragorna. HP Aragorna: {wojownik.hp}")

####################################
print("---", "Zadanie 20", "---")
####################################

from abc import ABC, abstractmethod # ABC pozwala utworzyć klasę abstrakcyjną
# anstractmethod ozn. metodę, którą klasy potomn muszą zaimplementować


class BaseTransformer(ABC):

    @abstractmethod
    def transform(self, dane):
        pass

    def fit(self, dane):
        pass


class DropNullTransformer(BaseTransformer):

    def transform(self, dane):
        wynik = []
        for i in dane:
            if i is not None:
                wynik.append(i)
        return wynik


class ClipTransformer(BaseTransformer):
    def fit(self, dane):
        self.minimum = min(dane)
        self.maksimum = max(dane)

    def transform(self, dane):

        wynik = []
        for i in dane:
            if i < self.minimum:
                i = self.minimum
                wynik.append(i)
            elif i > self.maksimum:
                i = self.maksimum
                wynik.append(i)
            else:
                wynik.append(i)
        return wynik


class SquareTransformer(BaseTransformer):
    def transform(self, dane):
        return [i ** 2 for i in dane]


class InverseTransformer(BaseTransformer):
    def transform(self, dane):
        return [1 / i for i in dane if i != 0]


class Pipeline:
    def __init__(self):
        self.kroki = []

    def dodaj_krok(self, krok):
        self.kroki.append(krok)

    def fit_transform(self, dane):
        wynik = dane
        for krok in self.kroki:
            krok.fit(wynik)
            wynik = krok.transform(wynik)
        return wynik


# Tworzenie pipeline'a z komponentów
pipeline = Pipeline()
pipeline.dodaj_krok(DropNullTransformer())
pipeline.dodaj_krok(ClipTransformer())
pipeline.dodaj_krok(SquareTransformer())
pipeline.dodaj_krok(InverseTransformer())

# Uruchomienie pipeline'a
dane_wejsciowe = [10, -5, 20, 30, -2, 40, 50]
wynik = pipeline.fit_transform(dane_wejsciowe)
print(wynik)
