"""
Tutaj jest link do repozytorium o moich projektach Data Science, które Panu pokazywałem na poprzedniej lekcji:
https://github.com/piotrgolebiewski07/data_science_projects

1. Tworzenie projektu w Django,
2. Analiza danych  i projekt ML w Pandas
3. html i css
"""

sep = "\n" + "-" * 5
sepa = "-" * 5
#################################################
print(sep, "Zadanie 1", sepa)
#################################################

temp = [22.5, 23.0, 21.5, 24.0, 23.5, 22.0, 23.0]
print(f'''{temp[0]}\n{temp[-1]}\n{temp[2:5]}''')

#################################################
print(sep, "Zadanie 2", sepa)
#################################################

results = []
results.append(0.75)
results.append(0.82)
results.append(0.79)
results.append(0.85)
results.append(0.88)
print(f"Lista results: {results}")
print(f"Długość listy: {len(results)}")
print(f"Średnia wartość: {sum(results) / len(results)}")
print(f"Maksymalna wartość: {max(results)}")
print(f"Minimalna wartość: {min(results)}")

#################################################
print(sep, "Zadanie 3", sepa)
#################################################
lista = [0.78, 0.92, 0.85, 0.88, 0.81, 0.95, 0.79]
lista.sort(reverse=True)
print(lista[:3])

#################################################
print(sep, "Zadanie 4", sepa)
#################################################

raw_col = " Customer ID "
print(raw_col.strip().lower().replace(" ", "_"))

#################################################
print(sep, "Zadanie 5", sepa)
#################################################

linia = "Alice,28,Data Scientist,75000"
pola = linia.split(",")
imie = pola[0]
wiek = pola[1]
zawod = pola[2]
pensja = pola[3]
print(f"{imie} ma {wiek} lat, pracuje jako {zawod} i zarabia ${pensja}.")

#################################################
print(sep, "Zadanie 6", sepa)
#################################################

model_name = "XGBoost"
accuracy = 0.8934
training_time = 45.67

print(f'''
Model: {model_name}
\tAccuracy: {accuracy:.2%}
\tTraining time: {training_time}
''')

#################################################
print(sep, "Zadanie 7", sepa)
#################################################

prediction = ['spam', 'ham', 'spam', 'spam', 'ham', 'ham', 'spam']
pred_spam = prediction.count("spam")
pred_ham = prediction.count("ham")
print(f"spam: {pred_spam}, ham: {pred_ham}")

#################################################
print(sep, "Zadanie 8", sepa)
#################################################

filename = "model_results_2024_Q3.csv"
filename_split = filename.split("_")
print(f"Rok: {filename_split[2]}\nKwartał: {filename_split[3][:2]}")
czy_csv = filename.endswith('.csv')
print(czy_csv)

#################################################
print(sep, "Zadanie 9", sepa)
#################################################

cm = [
[80, 10],   # TN, FP
[5, 45]     # FN, TP
]
print(cm)

TN = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]
TP = cm[1][1]

accuracy = (TP + TN) / (TP + TN + FP + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)

print(f"Accuracy: {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2f}")

#################################################
print(sep, "Zadanie 10", sepa)
#################################################

models = ['LogisticRegression', 'RandomForest', 'XGBoost', 'SVM']
models_string = ", ".join(models)
print(models_string)
model_sql = f"SELECT model FROM ({models_string})"
print(model_sql)

nowy_model = models_string.split(", ")
print(nowy_model)

print(models == nowy_model)

#################################################
print(sep, "Zadanie 11", sepa)
#################################################

log = "2024-01-15 10:23:45 ERROR Training failed due to OOM"
log_podzielony = log.split(" ", maxsplit=3)
print(f"[{log_podzielony[0]} {log_podzielony[1]}] {log_podzielony[2]}: {log_podzielony[3]}")

lista = ['INFO', 'WARNING', 'ERROR', 'DEBUG']
poziom_znany = log_podzielony[2] in lista
print(poziom_znany)

#################################################
print(sep, "Zadanie 12", sepa)
#################################################

tabela = "customers"
kolumny = ['id', 'name', 'email', 'city']
warunek = "city = 'New York'"
print(f"SELECT {', '.join(kolumny)} FROM {tabela} WHERE {warunek}")

#################################################
print(sep, "Zadanie 13", sepa)
#################################################

m1 = ['LogisticRegression', 0.78]
m2 = ['RandomForest', 0.92]
m3 = ['SVM', 0.85]
m4 = ['XGBoost', 0.95]

wszystkie = [m1, m2, m3, m4]
print(wszystkie)
accuracy = [m1[1], m2[1], m3[1], m4[1]]
accuracy.sort(reverse=True)
print(f"Top 3 wartości accuracy: {accuracy[:3]},\nmax accuracy = {max(accuracy)},\nmin accuracy = {min(accuracy)}")

#################################################
print(sep, "Zadanie 14", sepa)
#################################################

path = "/data/processed/2024/experiment_42_v3.csv"
path_lista = path.split('/')
print(path_lista)
print(f'''
{'Nazwa pliku:':<25} {path_lista[-1]}
{'Katalog:':<25} {"/".join(path_lista[:-1])}
{'Nazwa bez rozszerzenia:':<25} {path_lista[-1][:-4]}
{'Rozszerzenie:':<25} {path_lista[-1][-4:]}
{'Rok:':<25} {path_lista[3]}
''')

#################################################
print(sep, "Zadanie 15", sepa)
#################################################

kat_a = " Electronics "
kat_b = "ELECTRONICS"

kat_a_new = kat_a.strip().lower()
kat_b_new = kat_b.strip().lower()
print(kat_a_new == kat_b_new)
print(f"kat_a przed normalizacją: '{kat_a}' oraz po normalizacji: '{kat_a_new}'")
print(f"kat_b przed normalizacją: '{kat_b}' oraz po normalizacji: '{kat_b_new}'")

#################################################
print(sep, "Zadanie 16", sepa)
#################################################

e1 = ["Exp_01", 0.85, 1.23]
e2 = ["Exp_02", 0.89, 4.56]
e3 = ["Exp_03", 0.87, 7.89]

headers = ["Experimnet", "Accuracy", "Time (s)"]
print("=" * 44)
print(f"{headers[0]:<12}{headers[1]:>12}{headers[2]:>12}")
print("=" * 44)
print(f"{e1[0]:<12}{e1[1]:>12.2%}{e1[2]:>12}")
print(f"{e2[0]:<12}{e2[1]:>12.2%}{e2[2]:>12}")
print(f"{e3[0]:<12}{e3[1]:>12.2%}{e3[2]:>12}")
print("=" * 44)

#################################################
print(sep, "Zadanie 17", sepa)
#################################################

pole_imie=" Alice "
pole_wiek=" 28 "
pole_email=" alice@EXAMPLE.com "

pole_imie_czyste = pole_imie.strip()
pole_wiek_czyste = pole_wiek.strip()
pole_email_czyste = pole_email.strip().lower()

czy_imie_ok = pole_imie_czyste.isalpha()
czy_wiek_ok = pole_wiek_czyste.isdigit()
czy_email_ok = '@' in pole_email_czyste

print(f"""
Imię: {pole_imie_czyste}
Wiek: {pole_wiek_czyste}
Email: {pole_email_czyste}
Wszystkie pola OK? {czy_imie_ok and czy_wiek_ok and czy_email_ok}
""")

#################################################
print(sep, "Zadanie 18", sepa)
#################################################

e1 = ["Exp_01", 0.85, 1.23]
e2 = ["Exp_02", 0.89, 4.56]
e3 = ["Exp_03", 0.87, 7.89]

wiersze = [
    "# Raport",
    "| Experiment | Accuracy | Time |",
    "|------------|----------|------|",
    f"| {e1[0]} | {e1[1]:.2%} | {e1[2]}s |",
    f"| {e2[0]} | {e2[1]:.2%} | {e2[2]}s |",
    f"| {e3[0]} | {e3[1]:.2%} | {e3[2]}s |"
    ]

print("\n".join(wiersze))
