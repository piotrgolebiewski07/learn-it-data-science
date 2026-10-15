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


# ---------- Zadanie 9
print(sep, "Zadanie 9", sepa)

value_1 = 75
value_2 = 50
value_3 = 100
value_4 = 62.5
min_value = 50
max_value = 100

normalized_1 = (value_1 - min_value) / (max_value - min_value)
normalized_2 = (value_2 - min_value) / (max_value - min_value)
normalized_3 = (value_3 - min_value) / (max_value - min_value)
normalized_4 = (value_4 - min_value) / (max_value - min_value)
print(f"{normalized_1} mieści się w przedziale [0,1]: {0 <= normalized_1 <= 1}")
print(f"{normalized_2} mieści się w przedziale [0,1]: {0 <= normalized_2 <= 1}")
print(f"{normalized_3} mieści się w przedziale [0,1]: {0 <= normalized_3 <= 1}")
print(f"{normalized_4} mieści się w przedziale [0,1]: {0 <= normalized_4 <= 1}")
print("")
headers = ["wartość oryginalna", "wartość znormalizowana"]
print(f"{headers[0]:^25}{headers[1]:^25}")
print(f"{value_1:^25}{normalized_1:^25}\n{value_2:^25}{normalized_2:^25}\n{value_3:^25}{normalized_3:^25}\n{value_4:^25}{normalized_4:^25}")


# ---------- Zadanie 10
print(sep, "Zadanie 10", sepa)

nazwa_modelu = "XGBboost Classifier"
dataset = "Credit Card Fraud"
liczba_probek = 284807
accuracy = 0.9991
precision = 0.8876
recall = 0.7561
f1score = 2 * (precision * recall) / (precision + recall)

headers = ["Nazwa", "Wartość"]
print("=" * 52)
print(f"={headers[0]:^25}{headers[1]:^25}=")
print("=" * 52)
print(f"={'Nazwa modelu':^25}{nazwa_modelu:^25}=")
print(f"={'Dataset':^25}{dataset:^25}=")
print(f"={'Liczba próbek':^25}{liczba_probek:^25,}=")
print(f"={'Accuracy':^25}{accuracy:^25.2%}=")
print(f"={'Precision':^25}{precision:^25.2%}=")
print(f"={'Recall':^25}{recall:^25.2%}=")
print(f"={'F1-Score':^25}{f1score:^25.2%}=")
print("=" * 52)


# ---------- Zadanie 11
print(sep, "Zadanie 11", sepa)

import math

learning_rate = 0.01
batch_size = 64
epochs = 100
dropout = 0.5

if 0 < learning_rate <= 1:
    print("Learning rate: OK")
else:
    print("Learning rate: wartość poza zakresem")

if batch_size > 0 and math.log2(batch_size).is_integer():
    print("Batch size jest potęgą 2: OK")
else:
    print("Batch size nie jest potęgą 2.")

if 0 < epochs < 1000:
    print("Epochs mieści się w zakresie: OK")
else:
    print("Epochs: wartość poza zakresem")

if 0 <= dropout <= 1:
    print("Dropout mieści się w zakresie: OK")
else:
    print("Dropout: wartość poza zakresem")


# ---------- Zadanie 12
print(sep, "Zadanie 12", sepa)

liczba_probek = 50000
batch_size = 128
liczba_epok = 50
czas_na_batch = 0.15

liczba_pelnych_batchy = liczba_probek // batch_size
liczba_pozostalych_probek = liczba_probek % batch_size
print(f"Liczba pełnych batchów ({batch_size} próbek): {liczba_pelnych_batchy}")
print(f"Pozostałe próbki po podziale na batche: {liczba_pozostalych_probek}")

calkowita_liczba_batchy = liczba_pelnych_batchy + math.ceil((liczba_pozostalych_probek / batch_size))
print(f"Całkowita liczba batchy na 1 epokę: {calkowita_liczba_batchy} batchy")

czas = (liczba_pelnych_batchy * liczba_epok + (liczba_pozostalych_probek/batch_size) * liczba_epok) * czas_na_batch
print(f"Czas: {czas:.2f} s = {(czas / 60):.2f} min, {(czas / 3600):.2f} h (przy zał., że niepełny batch trwa proporcjonalnie krócej)")

print(f"Szacowany czas: {math.floor(czas/3600)} h {math.floor(czas / 60) % 60} min {round(((czas % 3600)/60-(math.floor(czas / 60) % 60))*60)} s")

