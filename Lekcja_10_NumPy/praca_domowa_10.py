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

####################################
print("\n---", "Zadanie 11", "---")
####################################

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

####################################
print("\n---", "Zadanie 13", "---")
####################################

np.random.seed(42)
data = np.concatenate([np.random.randn(100) * 10 + 50, np.array([150, -50, 200, -100, 180])])
np.random.shuffle(data)
print(f"Dane przed standaryzacją:\n{data}\n")

srednia = np.mean(data)
odchylenie = np.std(data)
z_score = (data - srednia) / odchylenie
print(f"Dane po standaryzacji:\n{np.round(z_score, 3)}\n")

outliery = z_score[abs(z_score) > 3]
print(f"Outliery: {np.round(outliery, 3)}")

data_bez_out = data[abs(z_score) <= 3]
srednia_bez_out = np.mean(data_bez_out)
odchylene_bez_out = np.std(data_bez_out)
z_score_bez_out = (data_bez_out - srednia_bez_out) / odchylene_bez_out
print(f"\nDane po standaryzacji bez outlierów:\n{np.round(z_score_bez_out, 3)}\n")

print(f"Statystyki przed:"
    f"Średnia: {srednia}\n"
    f"Odchylenie: {odchylenie}\n"
    f"Wartość min: {np.min(data)}\n"
    f"Wartośc max: {np.max(data)}\n"
    f"Liczba elementów: {len(data)}\n")

print(f"Statystyki po:"
    f"Średnia: {srednia_bez_out}\n"
    f"Odchylenie: {odchylene_bez_out}\n"
    f"Wartość min: {np.min(data_bez_out)}\n"
    f"Wartość max: {np.max(data_bez_out)}\n"
    f"Liczba elementów: {len(data_bez_out)}\n")

print("Histogram przed:")
bins = np.round(np.linspace(np.min(data), np.max(data), 31), 2)
counts, _ = np.histogram(data, bins=bins)

for i in range(len(bins)-1):
    bars = "█" * counts[i]
    print(f"Przedział od {bins[i]:^6} do {bins[i+1]:^6}: {bars}")

print("Histogram po:")
counts, _ = np.histogram(data_bez_out, bins=bins)

for i in range(len(bins)-1):
    bars = "█" * counts[i]
    print(f"Przedział od {bins[i]:^6} do {bins[i+1]:^6}: {bars}")
'''

####################################
print("\n---", "Zadanie 14", "---")
####################################

import numpy as np
x = np.linspace(-1, 1, 1000)
y = np.linspace(-1, 1, 1000)
X, Y = np.meshgrid(x, y) # meshgrid daje dwie macierze
punkty_w_kole = np.sum(X ** 2 + Y ** 2 <= 1) #można użyć np.count_nonzero(X ** 2 + Y ** 2 <= 1)

pi = 4 * (punkty_w_kole / (len(x) * len(y)))
print(pi)
blad = round(abs(pi - np.pi), 5)
print(f"Bład jest równy: {blad}")

x = np.linspace(-1, 1, 20)
y = np.linspace(-1, 1, 20)

X, Y = np.meshgrid(x, y)

punkty_w_kole = X ** 2 + Y ** 2 <= 1
print(punkty_w_kole)
print(np.where(punkty_w_kole, "●", "·"))

####################################
print("\n---", "Zadanie 15", "---")
####################################

signal = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=float)
kernel = np.array([0.2, 0.6, 0.2]) # średnia ruchoma ważona
result = []

for i in range(len(signal) - len(kernel) + 1):
    result.append(sum(signal[i:i+len(kernel)] * kernel))
print(np.array(result))

print(f"Sygnał (przed konwolucją)")
for i in signal:
    print("■" * int(i))

print(f"Wynik (po konwolucji)")
for i in result:
    print("■" * int(i))

####################################
print("\n---", "Zadanie 16", "---")
####################################

np.random.seed(5)
A = np.random.rand(10, 5) # 100 próbek × 50 cech

B = np.random.rand(5, 2) # 50 cech → 20 cech

C = A @ B
print(f"{C}\n")

D = np.zeros((10,2))
for i in range(A.shape[0]):
    for k in range(B.shape[1]):
        for j in range(A.shape[1]):
            D[i, k] += A[i, j] * B[j, k]

print(D)
print(np.allclose(C, D)) #sprawdza czy tablice zwierają takie same wartości (niewielka tolerancja błędu)

####################################
print("\n---", "Zadanie 17", "---")
####################################

np.random.seed(6)
image = np.random.randint(0, 256, size=(100, 100), dtype=np.uint8)
print(f"Image:\n{image}")

image[image < 128] = 0
image[image >= 128] = 255
print(f"\nImage (0, 255):\n{image}")

negatyw = 255 - image
print(f"\nNegatyw:\n{negatyw}")

pad_image = np.pad(negatyw, ((10, 10), (10, 10)))
print(f"\nPad image:\n{pad_image}")

print(f"\nShape image: {image.shape}\n"
    f"Shape negatyw: {negatyw.shape}\n"
    f"Shape pad_image: {pad_image.shape}\n")

print("Wartości progowe Image:"
    f"\n{image[:5, :5]}\n"
    f"\n{image[:5, -5:]}\n"
    f"\n{image[-5:, :5]}\n"
    f"\n{image[-5:, -5:]}\n")

print("Wartości progowe negatyw:"
    f"\n{negatyw[:5, :5]}\n"
    f"\n{negatyw[:5, -5:]}\n"
    f"\n{negatyw[-5:, :5]}\n"
    f"\n{negatyw[-5:, -5:]}\n")

print("Wartości progowe pad_image:"
    f"\n{pad_image[:5, :5]}\n"
    f"\n{pad_image[:5, -5:]}\n"
    f"\n{pad_image[-5:, :5]}\n"
    f"\n{pad_image[-5:, -5:]}\n")

####################################
print("\n---", "Zadanie 18", "---")
####################################

np.random.seed(10)
data = np.random.rand(50, 2) * 100
query = np.array([50.0, 50.0])

print(data)
print(query)

odl = np.round(np.sqrt(np.sum((query-data)**2, axis=1)), 2)
print(odl)

indeksy_najblizszych = np.argsort(odl)[:5]
print(odl[indeksy_najblizszych])

lista = ["indeks", "współrzędne", "odległość"]
print("=" * 55)
print(f"{lista[0]:^13} {lista[1]:^26} {lista[2]:^15}")
print("=" * 55)
for i in indeksy_najblizszych:
    print(f"{i:^13} {data[i]} {odl[i]:^15}")
print("=" * 55)

####################################
print("\n---", "Zadanie 19", "---")
####################################

np.random.seed(7)
x = np.linspace(0, 10, 100)
y = 2 * x**2 - 3 * x + 5 + np.random.randn(100) * 10

jedynki = np.ones((100, 1))
x_do_potegi = x ** 2

print("Pięć pierwszych wierszy macierzy X:")
macierz = np.column_stack((jedynki, x, x_do_potegi))
print(macierz[:5])
print("Pięć wartośći y:")
print(y[:5])

print("\nŚrednia i odchylenie standarodwe kolumny x²")
print(f"Średnia: {sum(macierz[:, 2] / len(macierz[:]))}")
print(f"Odcylenie standardowe: {np.std(macierz[:, 2])}")

####################################
print("\n---", "Zadanie 20", "---")
####################################

np.random.seed(8)
batch = np.random.randn(32, 10) * 5 + 20

# przed normalizacją
srednia = np.mean(batch[:], axis=0)
print(f"Średnia: {srednia}")

odchylenie = np.std(batch[:], axis=0)
print(f"Odchylenie: {odchylenie}")

# po normalizacji
batch_norm = (batch - srednia) / odchylenie
srednia_norm = np.mean(batch_norm[:], axis=0)
print(f"Średnia po normalizacji: {srednia_norm}")

odchylenie_norm = np.std(batch_norm[:], axis=0)
print(f"Odchylenie po  normalizacji: {odchylenie_norm}")

# po scale i shift
gamma = 2.0
beta = 1.0

output = gamma * batch_norm + beta

srednia_output = np.mean(output[:], axis=0)
print(f"Średnia po transformacji: {srednia_output}")

odchylenie_output = np.std(output[:], axis=0)
print(f"Odchylenie po  transformacji: {odchylenie_output}")

# Hisotgram przed
min_batch = np.min(batch[:, [0]])
max_batch = np.max(batch[:, [0]])

bins = np.linspace(min_batch, max_batch, 7)
print("Histogram przed:")
counts, _ = np.histogram(batch[:, 0], bins=bins)
for i in range(len(bins) - 1):
    bars = "█" * counts[i]
    print(f"Przedział od {bins[i]:^19} do {bins[i+1]:^19}: {bars}")
print()

# Hisotgram po normalizacji
min_norm = np.min(batch_norm[:, [0]])
max_norm = np.max(batch_norm[:, [0]])


bins = np.linspace(min_norm, max_norm, 7)
print("Histogram pp normalizacji:")
counts, _ = np.histogram(batch_norm[:, 0], bins=bins)
for i in range(len(bins) - 1):
    bars = "█" * counts[i]
    print(f"Przedział od {bins[i]:^19} do {bins[i+1]:^19}: {bars}")
print()

# Hisotgram po normalizacji
min_output = np.min(output[:, [0]])
max_output = np.max(output[:, [0]])


bins = np.linspace(min_output, max_output, 7)
print("Histogram pp transformacji:")
counts, _ = np.histogram(output[:, 0], bins=bins)
for i in range(len(bins) - 1):
    bars = "█" * counts[i]
    print(f"Przedział od {bins[i]:^19} do {bins[i+1]:^19}: {bars}")
