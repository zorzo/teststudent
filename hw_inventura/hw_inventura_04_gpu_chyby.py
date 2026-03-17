"""
Fáze 4: Přidání informací o grafické kartě (GPU) a ošetření chyb (try-except)
- Vyžaduje: pip install psutil py-cpuinfo gputil
- Zjišťování určitých parametrů HW může na některých PC selhat, proto učíme 'try-except'.
"""
import platform
import psutil
import cpuinfo

def get_gpu_info():
    """Pokusí se zjistit stav dedikovaných grafických karet (hlavně NVIDIA)."""
    try:
        import GPUtil
        gpus = GPUtil.getGPUs()
        if not gpus:
            print("GPU: Žádná dedikovaná NVIDIA GPU nenalezena (nebo chybí knihovny/ovladače).")
        for gpu in gpus:
            print(f"Grafická karta: {gpu.name}")
            print(f" -> Celková VRAM paměť: {gpu.memoryTotal} MB")
            print(f" -> Aktuální teplota: {gpu.temperature} °C")
    except ImportError:
        print("GPU upozornění: Knihovna 'GPUtil' není nainstalována.")
    except Exception as e:
        print(f"GPU chyba: Nepodařilo se načíst data o GPU. ({e})")

if __name__ == "__main__":
    print("=== Fáze 4: Detekce GPU a bloky try-except ===")
    
    # Bezpečné získání názvu CPU (může selhat třeba v emulátoru nebo kontejneru)
    try:
        info = cpuinfo.get_cpu_info()
        print(f"CPU: {info.get('brand_raw', 'Neznámý')}")
    except Exception:
        print("CPU: Detailní info o CPU se nepodařilo načíst.")
    
    get_gpu_info()

