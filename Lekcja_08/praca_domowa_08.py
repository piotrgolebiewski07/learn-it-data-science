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
print("---", "Zadanie 8", "---")
####################################

liczby = [-5, 3, -2, 8, 0, -1, 7, 4, -9, 6]

dodatnie = list(filter(lambda x: x > 0, liczby))
print(dodatnie)

podwojone = list(map(lambda x: x * 2, dodatnie))
print(podwojone)