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

'''
#################################################
print(sep, "Zadanie 13", sepa)
#################################################

#################################################
print(sep, "Zadanie 14", sepa)
#################################################

#################################################
print(sep, "Zadanie 15", sepa)
#################################################

#################################################
print(sep, "Zadanie 16", sepa)
#################################################

#################################################
print(sep, "Zadanie 17", sepa)
#################################################

#################################################
print(sep, "Zadanie 18", sepa)
#################################################

#################################################
print(sep, "Zadanie 19", sepa)
#################################################

#################################################
print(sep, "Zadanie 20", sepa)
#################################################
'''
