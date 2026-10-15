sep = "\n" + "-" * 5
sepa = "-" * 5
# ---------- Zadanie 1
print(sep, "Zadanie 1", sepa)

waga = 70
wzrost = 1.75

BMI = waga / (wzrost**2)
print(f"BMI: {BMI:.2f}")
if BMI < 18.5:
    print("Interpretacja: niedowaga")
elif 18.5 <= BMI < 25:
    print("Interpretacja: norma")
else:
    print("Interpretacja: nadwaga")


# ---------- Zadanie 2
print(sep, "Zadanie 2", sepa)

temperatura_celsius = 23.5
fahrenheit = temperatura_celsius * (9/5) + 32
kelvin = temperatura_celsius + 273.15

print(f"{temperatura_celsius:.1f}°C = {fahrenheit:.1f}°F = {kelvin:.1f} K")


# ---------- Zadanie 3
print(sep, "Zadanie 3", sepa)
liczba_probek = 1000

treningowy = 70 * liczba_probek // 100
walidacyjny = 15 * liczba_probek // 100
testowy = liczba_probek - treningowy - walidacyjny

suma = treningowy + walidacyjny + testowy
print(f"Całkowita liczba próbek: {suma}")

print(f"Zbiór treningowy: {treningowy}\nZbiór walidacyjny: {walidacyjny}\nZbiór testowy: {testowy}")


# ---------- Zadanie 4
print(sep, "Zadanie 4", sepa)

nazwa_raw = " PATIENT_age_YEARS"

print(nazwa_raw.strip().lower().replace("_", " ").title())


# ---------- Zadanie 5
print(sep, "Zadanie 5", sepa)

sciezka = "data/processed/train_fold_03_normalized.csv"

sciezka_elementy = sciezka.split("/")
nazwa_pliku, rozszerzenie = sciezka_elementy[2].split(".")
nazwa_pliku_ele = nazwa_pliku.split("_")

print(f"folder: {sciezka_elementy[0]}\nfolder podrzędny: {sciezka_elementy[1]}\ntyp zbioru: {nazwa_pliku_ele[0]}\nnumer fold: "
      f"{nazwa_pliku_ele[2]}\nformat pliku: {rozszerzenie}")


# ---------- Zadanie 6
print(sep, "Zadanie 6", sepa)

accuracy = 0.9234
precision = 0.8891
recall = 0.9456

headers = ["Accuraccy", "Precision", "Recall"]
print(f"{headers[0]:^15} {headers[1]:^15} {headers[2]:^15}")
print(f"{accuracy:^15.2%} {precision:^15.2%} {recall:^15.2%}")


# ---------- Zadanie 7
print(sep, "Zadanie 7", sepa)

accuracy_A = 0.87
accuracy_B = 0.89
train_time_A = 120
train_time_B = 450

accuracy_roznica = round(abs(accuracy_A - accuracy_B), 2)
print(accuracy_roznica)

time_roznica = train_time_A - train_time_B
print(time_roznica)

if (accuracy_roznica <= 0.02) and (accuracy_A < accuracy_B) and (train_time_A < train_time_B):
    print(f"Model A jest lepszym kompromisem ze względu na małą różnicę accuracy wynoszącą {accuracy_roznica}")


# ---------- Zadanie 8
print(sep, "Zadanie 8", sepa)

lr_initial = 0.1
decay = 0.95
epoch = 10

lr_new = lr_initial * (decay ** epoch)
print(f"Learning rate po {epoch} epokach: {lr_new:.2e}")

