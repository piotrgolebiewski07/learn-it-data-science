import numpy as np

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

