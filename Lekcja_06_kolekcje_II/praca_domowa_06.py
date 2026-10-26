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

#################################################
print(sep, "Zadanie 13", sepa)
#################################################

wyniki = {
      'LogReg': {'acc': 0.9667, 'prec': 0.9673, 'rec': 0.9667, 'f1': 0.9667},
      'DecisionTree': {'acc': 0.9333, 'prec': 0.9342, 'rec': 0.9333, 'f1': 0.9332},
      'RandomForest': {'acc': 0.9600, 'prec': 0.9610, 'rec': 0.9600, 'f1': 0.9601}
}
kolumny = ["Model", "Acc", "Prec", "Rec", "F1"]
wiersze = list(wyniki.keys())

print("=" * 60)
print(f"{kolumny[0]:<15} {kolumny[1]:<8} {kolumny[2]:<8} {kolumny[3]:<8} {kolumny[4]:<8}")
print("=" * 60)
print(f"{wiersze[0]:<15} {wyniki['LogReg']['acc']:<8.4f} {wyniki['LogReg']['prec']:<8.4f} {wyniki['LogReg']['rec']:<8.4f} {wyniki['LogReg']['f1']:<8.4f} ")
print(f"{wiersze[1]:<15} {wyniki['DecisionTree']['acc']:<8.4f} {wyniki['DecisionTree']['prec']:<8.4f} {wyniki['DecisionTree']['rec']:<8.4f} {wyniki['DecisionTree']['f1']:<8.4f} ")
print(f"{wiersze[2]:<15} {wyniki['RandomForest']['acc']:<8.4f} {wyniki['RandomForest']['prec']:<8.4f} {wyniki['RandomForest']['rec']:<8.4f} {wyniki['RandomForest']['f1']:<8.4f} ")
print("=" * 60)
print(f"Średnia acc: {(wyniki['LogReg']['acc'] + wyniki['DecisionTree']['acc'] + wyniki['RandomForest']['acc']) / 3:.4f}")
print(f"Średnia f1 : {(wyniki['LogReg']['f1'] + wyniki['DecisionTree']['f1'] + wyniki['RandomForest']['f1']) / 3:.4f}")

#################################################
print(sep, "Zadanie 14", sepa)
#################################################

dane = [
      ('setosa', 5.1, 3.5, 1.4, 0.2),
      ('setosa', 4.9, 3.0, 1.4, 0.2),
      ('versicolor', 7.0, 3.2, 4.7, 1.4),
      ('versicolor', 6.4, 3.2, 4.5, 1.5),
      ('virginica', 6.3, 3.3, 6.0, 2.5),
      ('virginica', 5.8, 2.7, 5.1, 1.9),
      ('setosa', 4.7, 3.2, 1.3, 0.2)
]

gatunki = {dane[0][0], dane[1][0], dane[2][0], dane[3][0], dane[4][0], dane[5][0], dane[6][0]}
print(gatunki)

print(f"Liczba unikalnych gatunków: {len(gatunki)}")
pierwszy_rekord = dane[0]
gatunek, sl, sw, pl, pw = pierwszy_rekord
sepal_length = [dane[0][1], dane[1][1], dane[2][1], dane[3][1], dane[4][1], dane[5][1], dane[6][1]]
print(f"Minimum: {min(sepal_length)}\n"
      f"Maksimum: {max(sepal_length)}\n"
      f"Suma: {sum(sepal_length)}\n"
      f"Średnia: {sum(sepal_length) / len(sepal_length):.3f}")

#################################################
print(sep, "Zadanie 15", sepa)
#################################################

wyniki = {
      'LogReg': {'acc': 0.9667, 'prec': 0.9673, 'rec': 0.9667, 'f1': 0.9667},
      'DecisionTree': {'acc': 0.9333, 'prec': 0.9342, 'rec': 0.9333, 'f1': 0.9332},
      'RandomForest': {'acc': 0.9600, 'prec': 0.9610, 'rec': 0.9600, 'f1': 0.9601}
}

print(wyniki)
slownik = {}

slownik['acc'] = {
      "LogReg": wyniki['LogReg']['acc'],
      "DecisionTree": wyniki['DecisionTree']['acc'],
      "RandomForest": wyniki['RandomForest']['acc'],
}
slownik['prec'] = {
      "LogReg": wyniki['LogReg']['prec'],
      "DecisionTree": wyniki['DecisionTree']['prec'],
      "RandomForest": wyniki['RandomForest']['prec'],
}
slownik['rec'] = {
      "LogReg": wyniki['LogReg']['rec'],
      "DecisionTree": wyniki['DecisionTree']['rec'],
      "RandomForest": wyniki['RandomForest']['rec'],
}
slownik['f1'] = {
      "LogReg": wyniki['LogReg']['f1'],
      "DecisionTree": wyniki['DecisionTree']['f1'],
      "RandomForest": wyniki['RandomForest']['f1'],
}
print(slownik)

print(f"acc: {max(slownik['acc'], key=slownik['acc'].get)} ({max(slownik['acc'].values())})")
print(f"prec: {max(slownik['prec'], key=slownik['prec'].get)} ({max(slownik['prec'].values())})")
print(f"rec: {max(slownik['rec'], key=slownik['rec'].get)} ({max(slownik['rec'].values())})")
print(f"f1: {max(slownik['f1'], key=slownik['f1'].get)} ({max(slownik['f1'].values())})")

zbior_najlepszych = set()
zbior_najlepszych.add(max(slownik['acc'], key=slownik['acc'].get))
zbior_najlepszych.add(max(slownik['prec'], key=slownik['prec'].get))
zbior_najlepszych.add(max(slownik['rec'], key=slownik['rec'].get))
zbior_najlepszych.add(max(slownik['f1'], key=slownik['f1'].get))
print(zbior_najlepszych)

#################################################
print(sep, "Zadanie 16", sepa)
#################################################

sprzedaz = {
      (2024, 'Q1'): 120_000,
      (2024, 'Q2'): 145_000,
      (2024, 'Q3'): 138_000,
      (2024, 'Q4'): 167_000,
      (2025, 'Q1'): 130_000,
      (2025, 'Q2'): 155_000,
      (2025, 'Q3'): 149_000
}

print(f"Suma: {sum(sprzedaz.values())}")

print(f"Wartość maksymalna: {max(sprzedaz.values())}")
print(f"Wartość minimalna: {min(sprzedaz.values())}")

rok_max, kw_max = max(sprzedaz, key=sprzedaz.get)
print(f"Najwyższa sprzedaż: {rok_max} {kw_max} - {max(sprzedaz.values())}")

posortowane_klucze = sorted(sprzedaz, key=sprzedaz.get, reverse=True)
print(posortowane_klucze[:3])

zbior_lat = set()
lata = list(sprzedaz)
zbior_lat.add(lata[0][0])
zbior_lat.add(lata[1][0])
zbior_lat.add(lata[2][0])
zbior_lat.add(lata[3][0])
zbior_lat.add(lata[4][0])
zbior_lat.add(lata[5][0])
zbior_lat.add(lata[6][0])
print(zbior_lat)

#################################################
print(sep, "Zadanie 17", sepa)
#################################################

wersja_1 = {'lr': 0.01, 'epochs': 100, 'optimizer': 'sgd', 'batch_size': 32, 'dropout': 0.2}
wersja_2 = {'lr': 0.001, 'epochs': 100, 'optimizer': 'adam', 'batch_size': 64, 'momentum': 0.9}

klucze_1 = set(wersja_1.keys())
klucze_2 = set(wersja_2.keys())
zbior_kluczy = klucze_1 | klucze_2
print(f"zbior kluczy: {zbior_kluczy}")

klucze_wspolne = klucze_1.intersection(klucze_2)
print(f"klucze wspólne: {klucze_wspolne}")

klucze_tylko_1 = klucze_1.difference(klucze_2)
print(f"klucze tylko z wersji 1: {klucze_tylko_1}")

klucze_tylko_2 = klucze_2.difference(klucze_1)
print(f"klucze tylko z wersji 2: {klucze_tylko_2}")

rozne_lr = wersja_1['lr'] != wersja_2['lr']
rozne_epochs = wersja_1['epochs'] != wersja_2['epochs']
rozne_optimizer = wersja_1['optimizer'] != wersja_2['optimizer']
rozne_batch_size = wersja_1['batch_size'] != wersja_2['batch_size']

print(f"lr różni się: {rozne_lr}")
print(f"epochs różni się: {rozne_epochs}")
print(f"optimizer różni się: {rozne_optimizer}")
print(f"batch_size różni się: {rozne_batch_size}")

#################################################
print(sep, "Zadanie 18", sepa)
#################################################

projekt = {
      'nazwa': 'iris_classification',
      'wersja': (1, 2, 0),
      'autorzy': {'Anna', 'Bartek', 'Cezary'},
      'dataset': {
            'nazwa': 'Iris',
            'shape': (150, 4),
            'klasy': ('setosa', 'versicolor', 'virginica')
      },
      'hiperparametry': {
            'lr': 0.001,
            'batch_size': 64,
            'epochs': 50
            }
}

major, minor, patch = projekt['wersja']
print(f"format: v{major}.{minor}.{patch}")

n_rekordów, n_cech = projekt["dataset"]["shape"]
print(f"Dataset Iris: {n_rekordów} × {n_cech}")

projekt["autorzy"].add("Dorota")
print(f"autorzy: {sorted(projekt['autorzy'])}, ilość: {len(projekt['autorzy'])}")

projekt["hiperparametry"].update({'dropout': 0.3, 'batch_size': 128})
print(projekt["hiperparametry"])

projekt["dataset"]["klasy"] = set(projekt["dataset"]["klasy"])
print(f"Czy 'setosa' jest w zbiorze klas:", "setosa" in projekt["dataset"]["klasy"])
