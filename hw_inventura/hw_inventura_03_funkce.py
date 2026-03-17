"""
Fáze 3: Refaktoring kódu do funkcí a detailnější CPU (knihovna 'py-cpuinfo')
- Vyžaduje: pip install psutil py-cpuinfo
- Učíme se strukturovat kód do znovupoužitelných funkcí.
"""
import platform
import psutil
import cpuinfo

def get_os_info():
    """Funkce pro získání informací o OS."""
    print(f"OS: {platform.system()} {platform.release()} ({platform.machine()})")

def get_cpu_info():
    """Funkce pro získání detailů o procesoru."""
    info = cpuinfo.get_cpu_info()
    # Použití metody .get() zabrání chybě, pokud hodnota neexistuje
    print(f"Procesor (čitelně): {info.get('brand_raw', 'Neznámý název')}")
    print(f"Jádra (Fyzická / Logická): {psutil.cpu_count(logical=False)} / {psutil.cpu_count(logical=True)}")
    print(f"Základní frekvence: {info.get('hz_advertised_friendly', 'Neznámá frekvence')}")

def get_ram_info():
    """Funkce pro získání informací o paměti."""
    svmem = psutil.virtual_memory()
    print(f"RAM Celkem: {svmem.total / (1024**3):.2f} GB")
    print(f"RAM Dostupná: {svmem.available / (1024**3):.2f} GB")

if __name__ == "__main__":
    print("=== Fáze 3: Refaktoring do funkcí ===")
    get_os_info()
    print("-" * 30)
    get_cpu_info()
    print("-" * 30)
    get_ram_info()

# Co si z toho zapamatovat:
# - Pokud skript roste, je dobré kód rozdělit do funkcí kvůli přehlednosti.
# - 'py-cpuinfo' dokáže získat skutečný obchodní název procesoru.
