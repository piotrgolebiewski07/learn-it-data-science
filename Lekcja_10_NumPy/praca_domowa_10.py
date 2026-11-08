'''import numpy as np

####################################
print("---", "Zadanie 1", "---")
####################################

tablica = np.arange(1, 101)
print(f"Suma: {np.sum(tablica)}\n"
    f"Średnia arytmetyczna: {np.mean(tablica)}\n"
    f"Mediana: {np.median(tablica)}\n"
    f"Maksimum: {np.max(tablica)}\n"
    f"Minimum: {np.min(tablica)}")

####################################
print("\n---", "Zadanie 2", "---")
####################################

before = np.array([100, 250, 75, 320, 180, 450, 90])
after = np.array([ 80, 200, 60, 280, 150, 400, 75])

print(before)
print(after)

print(f"Oszczędności: {before - after}\n"
    f"Rabat w %: {np.round((before - after) / before * 100, 2)}\n"
    f"Średnia oszczędność: {round(np.mean(before - after), 2)}")

####################################
print("\n---", "Zadanie 3", "---")
####################################

temps = np.array([15, 18, 22, 25, 23, 20, 17, 14, 16, 19, 21, 24])

print(f"Temperatura z dni parzystych: {temps[::2]}")
print(f"Ostatnie 5: {temps[-5:]}")
print(f"Odwrotna kolejnosć: {temps[::-1]}")

wieksze_od_20 = temps > 20
print(f"Większe od 20: {temps[wieksze_od_20]}")

####################################
print("\n---", "Zadanie 4", "---")
####################################
np.random.seed(0)

tablica = np.random.randint(1,51, size=(4, 5))
print(tablica)
print(f"wymiar: {tablica.shape}")
print(f"Drugi wiersz: {tablica[1]}")
print(f"Trzecia klumna: {tablica[:,2]}")
print(f"Element z pozycji (2, 3): {tablica[2, 3]}")

####################################
print("\n---", "Zadanie 5", "---")
####################################

np.random.seed(1)
sales = np.random.randint(10, 100, size=(4, 7))
print(sales)

print(f"Srednia produktu: {np.mean(sales, axis=1)}") #axis = 1 - wynik dla każdego wiersza
print(f"Srednia produktu: {np.mean(sales, axis=0)}") #axis = 1 - wynik dla każdej kolumny
print(f"Najwyższa dzienna sprzedaż: {np.argmax(np.sum(sales, axis=0))}")
print(f"Produkt z najniższą średnią sprzedażą: {np.argmin(np.mean(sales, axis=1))}")

####################################
print("\n---", "Zadanie 6", "---")
####################################

grades = np.array([78, 45, 92, 67, 34, 88, 56, 91, 23, 85, 73, 95])
print(f"Oceny (>=80): {grades[grades >= 80]}")
print(f"Oceny (<50): {grades[grades < 50]}")
print(f"Oceny (60-80): {grades[(grades >= 60) & (grades <= 80)]}")
grades_copy = grades.copy()
grades_copy[grades_copy < 50] = 50
print(f"Zmiana ocena na conajmniej 50: {grades_copy}")

####################################
print("\n---", "Zadanie 7", "---")
####################################

print(np.zeros((3, 3)))
print(np.ones((4, 4)))
print(np.eye(5))
print(np.full((3, 4), 7))
print(np.linspace(0, 1, 10))

####################################
print("\n---", "Zadanie 8", "---")
####################################

arr = np.arange(1, 13)
print(f"arr: {arr}")
arr = np.arange(1, 13).reshape(3, 4)
print(f"arr: {arr}")
arr = np.arange(1, 13).reshape(4, 3)
print(f"arr: {arr}")
arr = np.arange(1, 13).reshape(2, 6)
print(f"arr: {arr}")

a = arr.flatten()
print(f"arr spłasczona za pomocą flatten: {a}")

b = np.ravel(arr)
print(f"arr spłasczona za pomocą ravel: {b}")

a[0] = 100
print(a)
print(arr)

b[0] = 200
print(b)
print(arr)

print("Flatten tworzy kopię a ravel zwraca view - odwołuje się do tego samego miejsca w pamięci")

####################################
print("\n---", "Zadanie 9", "---")
####################################

np.random.seed(2)
scores = np.random.randint(40, 100, size=(20, 3))
print(scores)

min_vals = np.min(scores, axis=0)
max_vals = np.max(scores, axis=0)

normalized = (scores - min_vals) / (max_vals - min_vals)
print("Dane po normalizacji")
print(normalized)
min_vals_norm = np.min(normalized, axis=0)
max_vals_norm = np.max(normalized, axis=0)

print("\n=== Histogram przed ===")
# Histogram za pomocą np.histogram

for i in range(3):
    bins = np.linspace(min_vals[i], max_vals[i], 5)
    counts, edges = np.histogram(scores[:, i], bins)
    bars = " ".join("█" * c for c in counts)
    print(f" Przedmiot {i + 1}: {bars} counts={counts}")

print("\n=== Histogram po ===")
for i in range(3):
    bins = np.linspace(min_vals_norm[i], max_vals_norm[i], 5)
    counts, edges = np.histogram(normalized[:, i], bins)
    bars = " ".join("█" * c for c in counts)
    print(f" Przedmiot {i + 1}: {bars} counts={counts}")

####################################
print("\n---", "Zadanie 10", "---")
####################################

exams = np.array([
    [78, 85, 92, 88],
    [65, 72, 68, 70],
    [90, 88, 95, 92],
    [55, 60, 58, 62],
    [82, 79, 85, 80]
])
print(f"Exams:\n{exams}")

bonus = np.array([5, 10, 5, 10])
print(f"Exams + bonus:\n{exams + bonus}")

mnoznik = np.array([[1.0],
           [1.1],
           [0.95],
           [1.15],
           [1.0]])
print(f"Exams * mnoznik:\n{(exams + bonus) * mnoznik}")
'''
####################################
print("\n---", "Zadanie 11", "---")
####################################

import numpy as np
np.random.seed(3)
sales = np.random.randint(50, 200, size=(6, 28))
print(sales)
print(f"\nTrend sprzedaży: {np.sum(sales[:, -7:], axis=1) - np.sum(sales[:, :7], axis=1)}\n")

bins = np.linspace(0,28,5)

maksymalna = 0
tydzień = 1
for i in range(4):
    suma = np.sum(sales[:, int(bins[i]):int(bins[i+1])])
    print(f"Tydzień {i+1}: {suma}")

    if suma > maksymalna:
        maksymalna = suma
        tydzien = i+1

print(f"\nZ największa sprzedażą tydzień {tydzien}: {maksymalna}\n")

for i in range(6):
    suma = np.sum(sales[i, :])
    bars = "".join("█" * (suma // 100))
    print(f"Produk_{i+1}: {bars} {suma}")

####################################
print("\n---", "Zadanie 12", "---")
####################################

point_a = np.array([1, 2, 3, 4, 5])
point_b = np.array([5, 4, 3, 2, 1])

print(f"Odległość między a i b: {np.sqrt(sum((point_a - point_b) ** 2))}\n")

np.random.seed(4)
points = np.random.rand(4, 5)

zerowa = np.zeros((4, 4))

for i in range(4):
    for j in range(4):
        zerowa[i, j] = round(np.sqrt(sum((points[i] - points[j]) ** 2)), 3)

print(zerowa)



















