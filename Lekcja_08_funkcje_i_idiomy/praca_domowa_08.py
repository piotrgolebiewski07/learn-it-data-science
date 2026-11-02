####################################
print("---", "Zadanie 1", "---")
####################################


def statystyki(liczby):
    suma = sum(liczby)
    srednia = round(suma / len(liczby), 2)
    minimum = min(liczby)
    maksimum = max(liczby)

    return suma, srednia, minimum, maksimum


liczby = [3.5, 4.0, 5.0, 3.0, 4.5, 5.0, 4.0, 3.5]
suma, srednia, minimum, maksimum = statystyki(liczby)
print("Kalkulator statystyk:\n"
      f"Suma: {suma}\n"
      f"Średnia: {srednia}\n"
      f"Minimum: {minimum}\n"
      f"Maksimum: {maksimum}")


####################################
print("\n---", "Zadanie 2", "---")
####################################

celsius = [0, 10, 20, 30, 37, 100]


def celsius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f


def fahrenheit_to_celsius(f):
    c = (f - 32) * 5 / 9
    return c


def celsius_to_kelvin(c):
    k = c + 273.15
    return k


for c in celsius:
    print(f"{c:>3}°C = {celsius_to_fahrenheit(c):>5}°F = {celsius_to_kelvin(c):>6}K")


####################################
print("\n---", "Zadanie 3", "---")
####################################

parzyste = [i for i in range(1,101) if i % 2 == 0]
print(parzyste[:10])


####################################
print("\n---", "Zadanie 4", "---")
####################################

wynik = [i ** 2 for i in range(1, 21) if i % 2 != 0]
print(wynik)


####################################
print("\n---", "Zadanie 5", "---")
####################################

produkty = [
    ("laptop", 2999, 4.5),
    ("mysz", 89, 4.2),
    ("klawiatura", 249, 4.8),
    ("monitor", 899, 4.3)
]

produkty_sort_cena = sorted(produkty, key=lambda x: x[1])
print("Sortowanie po cenie:")
for prod in produkty_sort_cena:
    print(f"{prod[0]}, cena: {prod[1]}")

produkty_sort_ocena = sorted(produkty, key=lambda x: x[2], reverse=True)
print(f"\nSortowanie po ocenie:")
for prod in produkty_sort_ocena:
    print(f"{prod[0]}, ocena: {prod[2]}")

####################################
print("\n---", "Zadanie 6", "---")
####################################


def powitanie(imie, jezyk="polski"):
    if jezyk == "angielski":
        return f"Hello, {imie}!"
    elif jezyk == "niemiecki":
        return f"Hallo, {imie}!"
    else:
        return f"Cześć, {imie}!"

print(powitanie("Anna"))
print(powitanie("Anna", "angielski"))
print(powitanie("Anna", "niemiecki"))


####################################
print("\n---", "Zadanie 7", "---")
####################################

slowa = ["python", "data", "science", "machine", "learning", "AI"]

dlugosci = [len(i) for i in slowa]
print(dlugosci)

slownik_dlugosci = {slowo: dlugosc for slowo, dlugosc in zip(slowa, dlugosci)}
print(slownik_dlugosci)


####################################
print("\n---", "Zadanie 8", "---")
####################################

liczby = [-5, 3, -2, 8, 0, -1, 7, 4, -9, 6]

dodatnie = list(filter(lambda x: x > 0, liczby))
print(dodatnie)

podwojone = list(map(lambda x: x * 2, dodatnie))
print(podwojone)

####################################
print("\n---", "Zadanie 9", "---")
####################################

wynagrodzenia = [3500, 4200, 5800, 7200, 9500, 4800, 6100]
wynagrodzenia = sorted(wynagrodzenia)


def normalize_minmax_for(dane, zaokraglenie=3):

    minimum = min(dane)
    maksimum = max(dane)

    zakres = maksimum - minimum
    znormalizowane = []

    for i in dane:
        norma = (i - minimum) / zakres
        znormalizowane.append(round(norma, zaokraglenie))

    return znormalizowane


def normalize_minmax_comprehension(dane, zaokraglenie=3):
    minimum = min(dane)
    maksimum = max(dane)

    zakres = maksimum - minimum
    return [round(((i - minimum) / zakres), zaokraglenie) for i in dane]

print(f"Oryginalne wynagrodzenia: {wynagrodzenia}")
print(f"Normalizacja wynagrodzeń (for) : {normalize_minmax_for(wynagrodzenia)}")
print(f"Normalizacja wynagrodzeń (comprehension) : {normalize_minmax_comprehension(wynagrodzenia)}")


####################################
print("\n---", "Zadanie 10", "---")
####################################

transakcje = [
    {"produkt": "laptop", "wartosc": 2999},
    {"produkt": "mysz", "wartosc": 89},
    {"produkt": "laptop", "wartosc": 2999},
    {"produkt": "klawiatura", "wartosc": 249},
    {"produkt": "mysz", "wartosc": 89},
    {"produkt": "mysz", "wartosc": 89}
]

grouped = {}
for transakcja in transakcje:
    grouped.setdefault(transakcja["produkt"], 0)
    grouped[transakcja["produkt"]] += transakcja["wartosc"]

print(grouped)


####################################
print("\n---", "Zadanie 11", "---")
####################################

klienci = [
    {"id": 1, "wiek": 25, "dochod": 4500},
    {"id": 2, "wiek": 45, "dochod": 9200},
    {"id": 3, "wiek": 32, "dochod": 6800},
    {"id": 4, "wiek": 28, "dochod": 5200},
    {"id": 5, "wiek": 55, "dochod": 12000}
]


def kat_wiekowa(wiek):
    if wiek < 30:
        return "młody"
    elif wiek <= 50:
        return "średni"
    else:
        return "starszy"


def kat_dochod(dochod):
    if dochod < 5000:
        return "niski"
    elif dochod <= 10000:
        return "średni"
    else:
        return "wysoki"


klienci_wiek = [{**k, "kat_wiekowa": kat_wiekowa(k["wiek"])} for k in klienci]
print(klienci_wiek)

klienci_dochod = [{**k, "kat_dochodu": kat_dochod(k["dochod"])} for k in klienci_wiek]
print(klienci_dochod)


####################################
print("\n---", "Zadanie 12", "---")
####################################

tabela_mnozenia = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print("Macierz 10x10:")

for wiersz in tabela_mnozenia:
    print(" ".join(f"{x:3d}" for x in wiersz))

####################################
print("\n---", "Zadanie 13", "---")
####################################

sprzedaz = [
    (1, "elektronika", 45, 12500),
    (1, "odziez", 78, 4200),
    (2, "elektronika", 52, 15200),
    (2, "odziez", 65, 3800),
    (3, "elektronika", 38, 9800),
    (3, "odziez", 82, 5100),
    (4, "elektronika", 61, 18900),
    (4, "odziez", 71, 4500),
]


def tuple_to_dict(dane):
    return [{"Dzień": s[0], "Kategoria": s[1], "Liczba transakcji": s[2], "Wartość": s[3]} for s in dane]


sprzedaz_dict = tuple_to_dict(sprzedaz)
print("Sprzedaż dict:", sprzedaz_dict)


def dodaj_srednia_transakcji(dane):
    return dane.get("Wartość") / dane.get("Liczba transakcji")


def agreguj_po_kategorii(dane):
    kategorie = {}
    for dzien, kategoria, transakcje, wartosc in dane:
        kategorie[kategoria] = kategorie.get(kategoria, 0) + wartosc
    return kategorie


wynik_ze_srednia = [{**k, "Średnia na transakcję": round(dodaj_srednia_transakcji(k),2)} for k in sprzedaz_dict]

print("Kategorie z wartością:", agreguj_po_kategorii(sprzedaz))
print("Kategorie posortowane malejąco:", sorted(agreguj_po_kategorii(sprzedaz).items(), key=lambda x: x[1], reverse=True))

####################################
print("\n---", "Zadanie 14", "---")
####################################

czasy_odpowiedzi = [120, 135, 142, 128, 5000, 138, 145, 119, 10000, 133, 141]


def wykryj_outliery(dane):
    dane = sorted(dane)

    Q1 = dane[len(dane) // 4]
    Q3 = dane[3 * len(dane) // 4]
    IQR = Q3 - Q1

    czyste_dane = [i for i in dane if (Q1 - (1.5 * IQR)) <= i <= (Q3 + (1.5 * IQR))]
    outliery = [i for i in dane if (Q1 - (1.5 * IQR)) > i or i > (Q3 + (1.5 * IQR))]
    return czyste_dane, outliery


print(wykryj_outliery(czasy_odpowiedzi))

####################################
print("\n---", "Zadanie 15", "---")
####################################

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def applicator(func, iterable):
    return [func(i) for i in iterable]


def kwadraty(x):
    return x ** 2


def razy_10(x):
    return x * 10


def sqrt(x):
    return x ** 0.5


kwadraty_bez_map = applicator(kwadraty, liczby)
razy_10_bez_map = applicator(razy_10, liczby)
sqrt_bez_map = applicator(sqrt, liczby)

kwadraty_z_map = list(map(lambda x: x ** 2, liczby))
razy_10_z_map = list(map(lambda x: x * 10, liczby))
sqrt_z_map = list(map(lambda x: x ** 0.5, liczby))

print(f"Lista kwadratów (bez map): {kwadraty_bez_map}")
print(f"Lista kwadratów (z map): {kwadraty_z_map}")
print(f"Czy applicator zwraca to samo co z map: {kwadraty_bez_map == kwadraty_z_map}\n")

print(f"Lista liczb razy 10 (bez map): {razy_10_bez_map}")
print(f"Lista liczb razy 10(z map): {razy_10_z_map}")
print(f"Czy applicator zwraca to samo co z map: {razy_10_bez_map == razy_10_z_map}\n")

print(f"Lista pierwiastków (bez map): {sqrt_bez_map}")
print(f"Lista pierwiastków (z map): {sqrt_z_map}")
print(f"Czy applicator zwraca to samo co z map: {sqrt_bez_map == sqrt_z_map}")

####################################
print("\n---", "Zadanie 16", "---")
####################################


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


lista_fibo = [fibonacci(i) for i in range(15)]
print(lista_fibo)


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n-1)

print(silnia(10))

####################################
print("\n---", "Zadanie 17", "---")
####################################

n = 1000

lista = [i ** 2 for i in range(n)]
gen = (i ** 2 for i in range(n))

print(f"Lista obiekt typu: {type(lista)}, pierwszych pięć elementów listy: {lista[:5]}, len={len(lista)}")

lista_z_gen = []
licznik = 0

for i in gen:
    lista_z_gen.append(i)

    licznik += 1
    if licznik == 5:
        break
print(f"Generator obiekt typu: {type(gen)}, pierwszych pięć elementów: {lista_z_gen}, brak len()")
print("Lista tworzy wszystkie 1000 elementów od razu, a generator tylko pięć pierwszych")

####################################
print("\n---", "Zadanie 18", "---")
####################################


def k_fold_split(dane, k):
    return [dane[i * len(dane) // k:(i + 1) * len(dane) // k] for i in range(k)]

dane = list(range(1, 101))
k = 5

print(k_fold_split(dane, k))

####################################
print("\n---", "Zadanie 19", "---")
####################################

klienci = [
    {"id": 1, "wiek": 25, "dochod": 4500, "wydatki": 3200},
    {"id": 2, "wiek": 200, "dochod": 7800, "wydatki": 5100}, # outlier wiek
    {"id": 3, "wiek": 45, "dochod": 9200, "wydatki": -500}, # outlier wydatki
    {"id": 4, "wiek": 30, "dochod": 6000, "wydatki": 4000},
    {"id": 5, "wiek": 50, "dochod": 11000, "wydatki": 6500},
    {"id": 6, "wiek": 28, "dochod": 5000, "wydatki": 3500},
]


def usun_outliery(dane):
    klienci_wyczyszczone = []
    for klient in dane:
        if 0 <= klient["wiek"] <= 120 and klient["wydatki"] >= 0:
            klienci_wyczyszczone.append(klient)
    return klienci_wyczyszczone


def normalizuj_pole(dane, pole):
    lista_przed_normalizowaniem = []

    for i in dane:
        lista_przed_normalizowaniem.append(i[pole])

    minimum = min(lista_przed_normalizowaniem)
    maksimum = max(lista_przed_normalizowaniem)
    zakres = maksimum - minimum

    lista_po_znormalizowaniu = [{f"{pole}_norm": ((klient[pole] - minimum) / zakres)} for klient in dane]

    return [i | j for i, j in zip(dane, lista_po_znormalizowaniu)]


def segmentuj(dane):
    return [{**klient, "segment": "niski" if klient["dochod"] < 5000 else "sredni" if klient["dochod"] <= 10000 else "wysoki"} for klient in dane]


klienci_usun_outliery = usun_outliery(klienci)
klienci_dochod = normalizuj_pole(klienci_usun_outliery, "dochod")
klienci_dochod_wiek = normalizuj_pole(klienci_dochod, "wiek")

posortowana_lista = sorted(klienci_dochod_wiek, key=lambda x: x["dochod"])
print(f"Dane wyczyszczone z segmentami i znormalizowane: {segmentuj(posortowana_lista)}")

####################################
print("\n---", "Zadanie 20", "---")
####################################

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def my_map(func, iterable):
    wynik = []
    for i in iterable:
        wynik.append(func(i))
    return wynik


def my_filter(predicate, iterable):
    wynik = []
    for i in iterable:
        if predicate(i):
            wynik.append(i)
    return wynik


podwojone = my_map(lambda x: x * 2, liczby)
parzyste = my_filter(lambda x: x % 2 == 0, podwojone)

podwojone_map = list(map(lambda x: x * 2, liczby))
parzyste_filter = list(filter(lambda x: x % 2 == 0, podwojone_map))

print(f"my_map: {podwojone}")
print(f"map: {podwojone_map}")
print(f"my_filter: {parzyste}")
print(f"filter: {parzyste_filter}")

print(f"Czy wyniki map są takie same? {podwojone == podwojone_map}")
print(f"Czy wyniki filter są takie same? {parzyste == parzyste_filter}")

