sep = "\n" + "-" * 5
sepa = "-" * 5
#################################################
print(sep, "Zadanie 1", sepa)
#################################################

student = {"imie": "Kamil", "nazwisko": "Nowak", "wiek": 22, "kierunek": "Informatyka"}

print(student.get("imie"))
student['email'] = "kamil.nowak@edu.pl"
student["wiek"] = 23
print(f"Student: {student.get('imie')} {student.get('nazwisko')} ({student.get('wiek')} lata), "
      f"kierunek: {student.get('kierunek')}, email: {student.get('email')}")
print(list(student.keys()))
print(list(student.values()))

#################################################
print(sep, "Zadanie 2", sepa)
#################################################

konfig = {'lr': 0.01, 'epochs': 100, 'optimizer': 'adam'}
print(konfig.get("lr"))
print(konfig.get("momentum"))
print(konfig.get("momentum", 0.9))
print("batch_size" in konfig.keys())

#################################################
print(sep, "Zadanie 3", sepa)
#################################################

metryki = {"accuracy": 0.94, "precision": 0.91, "recall": 0.89, "f1_score": 0.90}
print(f"Najwyższa wartość: {max(metryki.values())}")
print(f"Najniższa wartość: {min(metryki.values())}")
print(f"Średnia wartość: {(sum(metryki.values())/len(metryki)):.3f}")
print(f"Klucze posortowane alfabetycznie: {sorted(metryki.keys())}")
print(f"Wartości posortowane rosnąco: {sorted(metryki.values())}")

#################################################
print(sep, "Zadanie 4", sepa)
#################################################

jezyki = ['Python', 'R', 'SQL', 'Python', 'Julia', 'R', 'Python', 'Scala', 'SQL']
unikalne = set(jezyki)
print(f"Zbiór unikalnych języków: {unikalne}")
print(f"Liczba unikalnych języków: {len(unikalne)}")
unikalne.update(["Go", "Rust"])
print(f"Zbiór uniklanych języków powiększony o dwa nowe: {unikalne}")
print(f"Czy Python w unikalnych: {'Python' in unikalne}")
print(f"Czy Fortran w unikalnych: {'Fortran' in unikalne}")
print(f"Czy Julia w unikalnych: {'Julia' in unikalne}")
unikalne.discard("Scala")
print(f"Finalny zbiór: {unikalne} o długości: {len(unikalne)}")

#################################################
print(sep, "Zadanie 5", sepa)
#################################################

grupa_a = {'python', 'pandas', 'numpy', 'sql', 'tableau'}
grupa_b = {'python', 'r', 'sql', 'ggplot2', 'dplyr'}

suma = grupa_a | grupa_b
suma_metoda = grupa_a.union(grupa_b)
print(f"Suma zbiorów: {suma}")
print(f"Suma zbiorów (metoda): {suma_metoda}")

iloczyn = grupa_a & grupa_b
iloczyn_metoda = grupa_a.intersection(grupa_b)
print(f"Iloczyn zbiorów: {iloczyn}")
print(f"Iloczyn zbiorów (metoda): {iloczyn_metoda}")

roznica_tylko_a = grupa_a - grupa_b
roznica_tylko_a_metoda = grupa_a.difference(grupa_b)
print(f"Elementy tylko z grupy a: {roznica_tylko_a}")
print(f"Elementy tylko z grupy a (metoda): {roznica_tylko_a_metoda}")

roznica_tylko_b = grupa_b - grupa_a
roznica_tylko_b_metoda = grupa_b.difference(grupa_a)
print(f"Elementy tylko z grupy b: {roznica_tylko_b}")
print(f"Elementy tylko z grupy b (metoda): {roznica_tylko_b_metoda}")

roznica_symetryczna = grupa_a ^ grupa_b
roznica_symetryczna_metoda = grupa_a.symmetric_difference(grupa_b)
print(f"Różnica symetryczna zbiorów: {roznica_symetryczna}")
print(f"Różnica symetryczna zbiorów (metoda): {roznica_symetryczna_metoda}")

print(f"Czy zbiory są rozłączne? {grupa_a.isdisjoint(grupa_b)}")

#################################################
print(sep, "Zadanie 6", sepa)
#################################################

wymiary = (1920, 1080)
szerokosc, wysokosc = wymiary
print(f"Rozdzielczość: {szerokosc}x{wysokosc}")

samotny = (42,)
print(type(samotny))
# samotny[0] = 100  - błąd TypeError

print(samotny + (100, 200))

#################################################
print(sep, "Zadanie 7", sepa)
#################################################

pracownik = ('Julia', 'Wiśniewska', 28, 'Data Analyst', 8500.0)
imie, nazwisko, wiek, stanowisko, pensja = pracownik

print(f"{imie} {nazwisko} ({wiek}) - {stanowisko}, pensja: {pensja:.2f} zł")

imie, *reszta = pracownik
print(f"imię: {imie}")
print(f"reszta: {reszta}")

#################################################
print(sep, "Zadanie 8", sepa)
#################################################

sprzedaz = {
      (2024, 'Q1'): 120_000,
      (2024, 'Q2'): 140_000,
      (2024, 'Q3'): 135_000,
      (2024, 'Q4'): 160_000
}

print(sprzedaz.get((2024, 'Q2')))
sprzedaz[(2025, 'Q1')] = 130_000
print(sprzedaz)

print(f"Najniższa wartość: {min(sprzedaz.values())}\n"
      f"Najwyższa wartość: {max(sprzedaz.values())}\n"
      f"Łączna sprzedaż: {sum(sprzedaz.values())}"
      )

klucze = list(sprzedaz.keys())
kwartaly = [klucze[0][1], klucze[1][1], klucze[2][1], klucze[3][1], klucze[4][1]]
zbior_kwartaly = set(kwartaly)
print(zbior_kwartaly)

print(len(zbior_kwartaly))

#################################################
print(sep, "Zadanie 9", sepa)
#################################################

domyslne = {'lr': 0.01, 'epochs': 100, 'optimizer': 'sgd', 'batch_size': 32}
uzytkownika = {'lr': 0.001, 'batch_size': 64, 'momentum': 0.9}

slownik_polaczony_1 = domyslne | uzytkownika
print(slownik_polaczony_1)

slownik_polaczony_2 = domyslne.copy()
slownik_polaczony_2.update(uzytkownika)
print(slownik_polaczony_2)

print(slownik_polaczony_1 == slownik_polaczony_2)

print(f"lr: {slownik_polaczony_1.get('lr')}\n"
      f"batch_size: {slownik_polaczony_1.get('batch_size')}\n"
      f"momentum: {slownik_polaczony_1.get('momentum')}\n")

#################################################
print(sep, "Zadanie 10", sepa)
#################################################

dataset_a = {'wiek', 'plec', 'miasto', 'dochod', 'wyksztalcenie', 'stan_cywilny'}
dataset_b = {'wiek', 'plec', 'miasto', 'pensja', 'stanowisko', 'staz'}

czesc_wspolna = dataset_a.intersection(dataset_b)
print(czesc_wspolna)

tylko_a = dataset_a.difference(dataset_b)
print(tylko_a)

tylko_b = dataset_b.difference(dataset_a)
print(tylko_b)

suma = dataset_a.union(dataset_b)
print(suma)

roznica_symetryczna = dataset_a.symmetric_difference(dataset_b)
print(roznica_symetryczna)

print({'wiek', 'plec'}.issubset(czesc_wspolna))

#################################################
print(sep, "Zadanie 11", sepa)
#################################################

raport = {
      'Q1': {'przychod': 120_000, 'koszt': 80_000},
      'Q2': {'przychod': 145_000, 'koszt': 92_000},
      'Q3': {'przychod': 138_000, 'koszt': 88_000},
      'Q4': {'przychod': 167_000, 'koszt': 101_000}
      }

print(f"Q1: {raport.get('Q1').get('przychod')}\n"
      f"Q2: {raport.get('Q2').get('przychod')}\n"
      f"Q3: {raport.get('Q3').get('przychod')}\n"
      f"Q4: {raport.get('Q4').get('przychod')}")

raport['Q1']['zysk'] = raport['Q1']['przychod']-raport['Q1']['koszt']
raport['Q2']['zysk'] = raport['Q2']['przychod']-raport['Q2']['koszt']
raport['Q3']['zysk'] = raport['Q3']['przychod']-raport['Q3']['koszt']
raport['Q4']['zysk'] = raport['Q4']['przychod']-raport['Q4']['koszt']
print(f"Q1 | {raport['Q1']['przychod']:>8} | {raport['Q1']['koszt']:>8} | {raport['Q1']['zysk']:>8}\n"
      f"Q2 | {raport['Q2']['przychod']:>8} | {raport['Q2']['koszt']:>8} | {raport['Q2']['zysk']:>8}\n"
      f"Q3 | {raport['Q3']['przychod']:>8} | {raport['Q3']['koszt']:>8} | {raport['Q3']['zysk']:>8}\n"
      f"Q4 | {raport['Q4']['przychod']:>8} | {raport['Q4']['koszt']:>8} | {raport['Q4']['zysk']:>8}\n")

print(raport)
lista_zyskow = [
      raport.get('Q1').get('zysk'),
      raport.get('Q2').get('zysk'),
      raport.get('Q3').get('zysk'),
      raport.get('Q4').get('zysk')
]
print(lista_zyskow)
print(f"Suma zysków: {sum(lista_zyskow)}")
print(f"Minimum: {min(lista_zyskow)}")
print(f"Maksimum: {max(lista_zyskow)}")
print(f"Średnia: {sum(lista_zyskow) / len(lista_zyskow)}")

#################################################
print(sep, "Zadanie 12", sepa)
#################################################

rekord = ('setosa', 5.1, 3.5, 1.4, 0.2)

gatunek, sl, sw, pl, pw = rekord
rekord_slownik = {
      'species': gatunek,
      'sepal_length': sl,
      'sepal_width': sw,
      'petal_length': pl,
      'petal_width': pw
}
#print(f"{species:<13} :{gatunek:<13}")
print(f"{list(rekord_slownik.keys())[0]:<13}: {rekord_slownik['species']:>5}")
print(f"{list(rekord_slownik.keys())[1]:<13}: {sl:>5.1f}")
print(f"{list(rekord_slownik.keys())[2]:<13}: {sw:>5.1f}")
print(f"{list(rekord_slownik.keys())[3]:<13}: {pl:>5.1f}")
print(f"{list(rekord_slownik.keys())[4]:<13}: {pw:>5.1f}")

print(f"Suma cech: {sum(rekord[1:])}")
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


