"""
Fáze 2: Přidání knihovny 'psutil' pro paměť a disky
- Vyžaduje instalaci: pip install psutil
- Začínáme pracovat s hardwarem mimo procesor - zjišťujeme RAM a disky.
"""
import platform
import psutil

print("=== Fáze 2: OS, Paměť a disky ===")
print(f"OS: {platform.system()} {platform.release()} ({platform.machine()})")

print("\n--- Procesor (CPU) ---")
print(f"Fyzická jádra CPU: {psutil.cpu_count(logical=False)}")
print(f"Logická jádra CPU (vlákna): {psutil.cpu_count(logical=True)}")

print("\n--- Operační paměť (RAM) ---")
svmem = psutil.virtual_memory()
# Převod z bytů na gigabyty (GB)
ram_gb = svmem.total / (1024 ** 3)
print(f"Celková RAM: {ram_gb:.2f} GB")

print("\n--- Pevné disky ---")
for partition in psutil.disk_partitions():
    print(f"Disk: {partition.device} | Typ souborového systému: {partition.fstype} | Připojeno do: {partition.mountpoint}")

# Co si z toho zapamatovat:
# - 'psutil' je nejlepší multiplatformní nástroj na informace o systému v Pythonu.
# - Velikosti paměti a disků bývají v bytech, je nutné je přepočítat na MB nebo GB.
