sep = "\n" + "-" * 5
sepa = "-" * 5
#################################################
print(sep, "Zadanie 1", sepa)
#################################################

liczby = [12, 7, 23, 45, 8, 19, 34, 56, 91, 2]

for liczba in liczby:
    if liczba % 2 == 0:
        print(f"{liczba} - parzysta")
    else:
        print(f"{liczba} - nieparzysta")

#################################################
print(sep, "Zadanie 2", sepa)
#################################################

temperatury = [-5, 3, -2, 8, 12, -1, 6, 0, 15, -3]
suma = 0
ile = 0

for temp in temperatury:
    if temp > 0:
        suma += temp
        ile += 1
print(f"Suma wynosi: {suma}")
print(f"Dodatnich temperatur jest: {ile}")

#################################################
print(sep, "Zadanie 3", sepa)
#################################################

for i in range(20, -1, -2):
    print(i)

#################################################
print(sep, "Zadanie 4", sepa)
#################################################

wyniki = [78, 92, 65, 88, 95, 71, 85]
maksimum = wyniki[0]

for wynik in wyniki:
    if wynik > maksimum:
        maksimum = wynik

print(maksimum)

#################################################
print(sep, "Zadanie 5", sepa)
#################################################

ile = 1
suma = 0

while ile <= 50:
    suma += ile
    ile += 1
print(f"Suma liczb od 1 do 50: {suma}")

n = 50
print(f"Ze wzoru suma równa jest: {n * (n+1) / 2:.0f}")

#################################################
print(sep, "Zadanie 6", sepa)
#################################################

temperatury = [36.5, 37.8, 36.2, 38.5, 36.9, 39.2, 37.0]
liczba_goraczek = 0
for temp in temperatury:
    if temp >= 38:
        print(f"gorączka: {temp}°C")
        liczba_goraczek += 1

print(f"Odsetek przpadków z gorączką: {liczba_goraczek / len(temperatury) * 100:.2f}%")

#################################################
print(sep, "Zadanie 7", sepa)
#################################################

for i in range(1, 11):
    dzialanie = f"7 × {i}"
    print(f"{dzialanie:<8} = {7 * i}")

#################################################
print(sep, "Zadanie 8", sepa)
#################################################

wzrosty_cm = [165, 178, 182, 159, 171, 190]
wzrosty_m = [i / 100 for i in wzrosty_cm]

print(f"wzrost w cm: {wzrosty_cm}")
print(f"wzrost w m: {wzrosty_m}")

#################################################
print(sep, "Zadanie 9", sepa)
#################################################

wagi = [70, 85, 62, 95, 78]
wzrosty = [1.75, 1.80, 1.65, 1.78, 1.72]

for i in range(len(wagi)):
    bmi = wagi[i] / wzrosty[i] ** 2
    opis_bmi = ""
    if bmi < 18.5:
        opis_bmi = "niedowaga"
    elif 18.5 <= bmi < 25:
        opis_bmi = "norma"
    elif 25 <= bmi < 30:
        opis_bmi = "nadwaga"
    elif bmi >= 30:
        opis_bmi = "otyłość"
    print(f"Pacjent {i+1}: waga {wagi[i]} kg, wzrost {wzrosty[i]:.2f} m, BMI {bmi:.2f} - {opis_bmi}")

#################################################
print(sep, "Zadanie 10", sepa)
#################################################

ilosc = 0
pierwsze = []

for i in range(2, 101):
    czy_pierwsza = True

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            czy_pierwsza = False
            break

    if czy_pierwsza:
        pierwsze.append(i)
        ilosc += 1

print(f"Ilość liczb pierwszych: {ilosc}")
print(f"Lista liczb pierwszych: {pierwsze}")

#################################################
print(sep, "Zadanie 11", sepa)
#################################################

sprzedaz = [1200, 1350, 1290, 1480, 1520, 1510, 1680, 1720, 1700, 1890, 1950, 2100]
liczba_miesiecy_ze_wzrostem = 0
liczba_miesiecy_ze_spadkiem = 0
lista_wzrostu = []

for i in range(1,12):
    if sprzedaz[i] > sprzedaz[i-1]:
        wzrost = sprzedaz[i] / sprzedaz[i - 1] - 1
        print(f"Miesiąc {i+1}: wzrost z {sprzedaz[i-1]} do {sprzedaz[i]} (+{wzrost:.2%})")
        liczba_miesiecy_ze_wzrostem += 1
        lista_wzrostu.append(wzrost)
    elif sprzedaz[i] < sprzedaz[i-1]:
        liczba_miesiecy_ze_spadkiem += 1

print(f"Liczba miesięcy ze wzrostem: {liczba_miesiecy_ze_wzrostem}")
print(f"Liczba miesięcy ze spadkiem: {liczba_miesiecy_ze_spadkiem}")
print(f"Średni miesięczny wzrost: {sum(lista_wzrostu) / len(lista_wzrostu):.2%}")

#################################################
print(sep, "Zadanie 12", sepa)
#################################################

pesele = ['92041812345', '8501015432', 'abc123', '78121698765']

for pesel in pesele:
    if len(pesel) == 11 and pesel.isdigit():
        print(f"PESEL {pesel}: poprawny format")
    else:
        print(f"PESEL {pesel}: błędny format (długość {len(pesel)})")

#################################################
print(sep, "Zadanie 13", sepa)
#################################################

trening = [(1.5, 'A'), (2.3, 'A'), (3.8, 'B'), (4.2, 'B'), (5.1, 'B')]
x_nowy = 3.5

lista_treningowa = [(abs(x_nowy - x), klasa) for x, klasa in trening]
nowa_lista_treningowa = sorted(lista_treningowa)

k = 3
klasa_a = 0
klasa_b = 0

for i in range(k):
    if nowa_lista_treningowa[i][1] == "A":
        klasa_a += 1
    else:
        klasa_b += 1

print(f"Klasa A: {klasa_a}")
print(f"Klasa B: {klasa_b}")

print(nowa_lista_treningowa[:k])

print(f"Przewidywana klasa to: {'A' if klasa_a > klasa_b else 'B'}")

#################################################
print(sep, "Zadanie 14", sepa)
#################################################

wzrost = [165, 170, 175, 180, 185]
waga = [60, 65, 70, 75, 80]

sr_x = sum(wzrost) / len(wzrost)
print(sr_x)

sr_y = sum(waga) / len(waga)
print(sr_y)

sum_xy = 0
sum_x2 = 0
sum_y2 = 0

for i in range(len(wzrost)):
    sum_xy += (wzrost[i] - sr_x) * (waga[i] - sr_y)
    sum_x2 += (wzrost[i] - sr_x) ** 2
    sum_y2 += (waga[i] - sr_y) ** 2

r = sum_xy / (sum_x2 * sum_y2) ** 0.5
print(f"{r:.4f}")

#################################################
print(sep, "Zadanie 15", sepa)
#################################################

wyniki = [78, 82, 85, 88, 90, 92, 95, 97, 99, 45, 101, 103, 105, 180]

posort = sorted(wyniki)
print(posort)

Q1 = posort[len(posort) // 4]
print(f"Q1 = {Q1}")

Q3 = posort[3 * len(posort) // 4]
print(f"Q3 = {Q3}")

IQR = Q3 - Q1
print(f"IQR = {IQR}")

granice = [Q1 - 1.5 * IQR, Q3 + 1.5 * IQR]
print(f"Granice dolna i górna: {granice}")

outliers = [x for x in wyniki if x < granice[0] or x > granice[1]]
print(f"Lista outliers: {outliers}")

#################################################
print(sep, "Zadanie 16", sepa)
#################################################

import math
n = 1_000_000
suma = 0

for i in range(n):
    licznik = (-1) ** i
    mianownik = 2 * i + 1
    suma += licznik / mianownik

aproksymacja_liczby_pi = suma * 4
print(f"Wyliczona liczba pi: {aproksymacja_liczby_pi:.6f}")
liczba_pi = math.pi
print(f"Liczba pi: {round(liczba_pi, 6)}")

blad = abs(aproksymacja_liczby_pi - round(liczba_pi, 6))
print(f"Błąd: {blad:.6f}")

#################################################
print(sep, "Zadanie 17", sepa)
#################################################

a = 252
b = 105

iteracje = 0
while b != 0:
    a, b = b, a % b
    iteracje += 1

print(f"NWD = {a}")
print(f"Liczba iteracji: {iteracje}")

#################################################
print(sep, "Zadanie 18", sepa)
#################################################

dane = [12, 15, 18, 22, 25, 28, 31, 35, 38, 42, 45, 48, 52, 55, 58]
granice = [10, 20, 30, 40, 50, 60]
biny = [0, 0, 0, 0, 0]

for x in dane:
    for i in range(5):
        if granice[i] <= x < granice[i+1]:
            biny[i] += 1
            break

for i in range(len(biny)):
    print(f"[{granice[i]}, {granice[i+1]}): {'*' * biny[i]}")

#################################################
print(sep, "Zadanie 19", sepa)
#################################################

stany = ['A', 'B', 'A', 'A', 'C', 'B', 'C', 'A', 'B', 'B']

unikalne = sorted(set(stany))
przejscia = {}

for i in unikalne:
    for j in unikalne:
        przejscia.setdefault(i, {}).setdefault(j, 0)

print(przejscia)

for i in range(len(stany)-1):
    przejscia[stany[i]][stany[i+1]] += 1

print(przejscia)
print("  A B C")
for i in unikalne:
    print(i, end=" ")
    for j in unikalne:
        print(przejscia[i][j], end=" ")
    print()

#################################################
print(sep, "Zadanie 20", sepa)
#################################################

dane = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

min_dane = dane[0]
max_dane = dane[0]

for i in dane:
    if min_dane > i:
        min_dane = i
    if max_dane < i:
        max_dane = i

z_norm = [(x - min_dane) / (max_dane - min_dane) for x in dane]
print(z_norm)
print("Wyniki weryfikacji:")
print(z_norm[0], z_norm[0] == 0.0)
print(z_norm[-1], z_norm[-1] == 1.0)