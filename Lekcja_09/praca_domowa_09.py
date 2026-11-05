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
        self.wlasciciel= wlasciciel
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
        self.pensja = self.pensja * (1 + self.procent/ 100)

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
        return(wynik)

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
print("---", "Zadanie 11", "---")
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
