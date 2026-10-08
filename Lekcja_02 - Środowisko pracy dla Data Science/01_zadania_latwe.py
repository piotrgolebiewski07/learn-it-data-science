import sys
import psutil
import platform
import numpy as np

# Zadanie 1
print("--- Informacje o systemie --- ")
print(f"System operacyjny: {platform.system()} {platform.release()}")
print(f"Python version: {sys.version}")
print()

print("--- Pamięć RAM ---")
print(f"Całkowita RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB")
print(f"Dostępna RAM: {psutil.virtual_memory().available / (1024**3):.2f} GB")
print()

try:
    import torch
    if torch.cuda.is_available():
        print("---GPU---")
        print("GPU dostępne: TAK")
        print(f"Nazwa GPU: {torch.cuda.get_device_name(0)}")
        print(f"Pamięć GPU: {torch.cuda.get_device_properties(0).total_memory / (1024**3):.2f} GB")

        print("Wersja PyTorch:", torch.__version__)
        print("Wersja CUDA:", torch.version.cuda)
        print("GPU dostępne:", torch.cuda.is_available())
    else:
        print("Wersja PyTorch:", torch.__version__)
        print("Wersja CUDA:", torch.version.cuda)
        print("GPU dostępne:", torch.cuda.is_available())
        print("GPU przez CUDA niedostępne - PyTorch korzysta z CPU")
except ImportError:
    print("PyTorch niezainstalowany - nie można sprawdzić GPU")

'''
--- Informacje o systemie --- 
System operacyjny: Windows 10
Python version: 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)]

--- Pamięć RAM ---
Całkowita RAM: 15.87 GB
Dostępna RAM: 4.43 GB

---GPU---
GPU dostępne: TAK
Nazwa GPU: NVIDIA GeForce GTX 1650
Pamięć GPU: 4.00 GB
Wersja PyTorch: 2.13.0+cu126
Wersja CUDA: 12.6
GPU dostępne: True
'''

# Zadania 2 i 3 dotyczą google colab - nie używam

# Zadanie 4
# Obrazek: materialy/zadanie_4_venv.png

# Zadanie 5
import os

project_structure = {
    'data': ['raw', 'processed'],
    'notebooks': [],
    'src': [],
    'models': [],
    'reports': []
}


def create_project_structure(project_name, structure):
    os.makedirs(project_name, exist_ok=True)
    print(f"Utworzono projekt: {project_name}/")

    for folder, subfolders in structure.items():
        folder_path = os.path.join(project_name, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f" ├── {folder}/")

        for subfolder in subfolders:
            subfolder_path = os.path.join(folder_path, subfolder)
            os.makedirs(subfolder_path, exist_ok=True)
            print(f" | ├── {subfolder}/")

    files_to_create = {
        "README.md": f'# {project_name}\n\nOpis projektu DS do lekcji 2.',
        '.gitignore': 'data/raw/',
    }

    for filename, content in files_to_create.items():
        filepath = os.path.join(project_name, filename)
        with open(filepath, 'w') as f:
            f.write(content)
        print(f" ├── {filename}")

    print(f"\n Struktura projektu ' {project_name}' utworzona.")


create_project_structure('sales_analysis', project_structure)

# Zadanie 6 — rozwiązanie w notebooku:
# materialy/lesson02_practice.ipynb


# Zadanie 7
def monitorowanie_zuzycia_zasobow():
    start_cpu = psutil.cpu_percent(interval=1)
    start_ram = psutil.virtual_memory().used / (1000**3)

    macierz = np.random.rand(1000, 1000)
    odwrotna = np.linalg.inv(macierz)

    koniec_cpu = psutil.cpu_percent()
    koniec_ram = psutil.virtual_memory().used / (1000**3)

    wartosc_cpu = koniec_cpu - start_cpu
    wartosc_ram = koniec_ram - start_ram

    print(f"CPU przed: {start_cpu:.1f}%")
    print(f"CPU podczas obliczeń: {koniec_cpu:.1f}%")
    print(f"Różnica CPU: {wartosc_cpu:.1f} pp")

    print(f"RAM przed: {start_ram:.4f}GB")
    print(f"RAM po obliczeniach: {koniec_ram:.4f}GB")
    print(f"Różnica RAM: {wartosc_ram:.4f}GB = {wartosc_ram * 1000:.1f}MB")


monitorowanie_zuzycia_zasobow()
'''
CPU przed: 7.8%
CPU podczas obliczeń: 39.6%
Różnica CPU: 31.8 pp
RAM przed: 12.1157GB
RAM po obliczeniach: 12.1331GB
Różnica RAM: 0.0173GB = 17.3MB
'''