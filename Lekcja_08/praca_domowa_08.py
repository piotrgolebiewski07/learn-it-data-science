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



