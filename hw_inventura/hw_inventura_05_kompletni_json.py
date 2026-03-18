"""
Fáze 5: Komplexní inventura - detaily pro Windows a hromadný export dat do JSONu
- Vyžaduje (na Windows): pip install psutil py-cpuinfo gputil wmi
- Cílem už není jen výpis do konzole, ale vytvoření datového slovníku pro další zpracování
  (např. uložení na server, sběr dat z celé školy).
"""
import os
import platform
import psutil
import json
import cpuinfo

def get_system_data():
    """Shromáždí všechna dostupná data do podoby Python slovníku (dictionary)."""
    data = {
        "os": {
            "system": platform.system(),
            "release": platform.release(),
            "architecture": platform.machine()
        },
        "cpu": {},
        "ram": {},
        "motherboard": {}
    }
    
    # 1. CPU
    # Používáme try-except, program by neměl spadnout, pokud balíček cpuinfo chybí,
    # nebo nedokáže rozpoznat procesor. V takovém případě slovník zůstane jen s defaultními klíči.
    try:
        c_info = cpuinfo.get_cpu_info()
        data["cpu"]["model"] = c_info.get("brand_raw", platform.processor())
        data["cpu"]["cores_physical"] = psutil.cpu_count(logical=False)
        data["cpu"]["cores_logical"] = psutil.cpu_count(logical=True)
    except Exception as e:
        data["cpu"]["error"] = f"Nelze načíst CPU info: {e}"

    # 2. RAM
    svmem = psutil.virtual_memory()
    data["ram"]["total_gb"] = round(svmem.total / (1024**3), 2)
    
    # 3. Základní deska (ukázka OS specifického přístupu pro Windows)
    if platform.system() == "Windows":
        # Blok try-except zde ošetřuje chybu při chybějící knihovně (ImportError) a
        # případné další chyby při komunikaci s Windows Management Instrumentation (WMI).
        try:
            import wmi
            c = wmi.WMI()
            # Třída Win32_BaseBoard obsahuje nízkoúrovňová data o základní desce počítače.
            board = c.Win32_BaseBoard()[0]
            data["motherboard"]["manufacturer"] = board.Manufacturer
            data["motherboard"]["product"] = board.Product
        except ImportError:
            data["motherboard"]["error"] = "Knihovna WMI není nainstalována."
        except Exception as e:
            data["motherboard"]["error"] = f"WMI chyba při čtení desky: {e}"
    else:
        # Ponecháno pro Mac a Linux
        data["motherboard"]["message"] = "Tento skript zatím podporuje detailní info o desce jen na Windows."

    return data

if __name__ == "__main__":
    print("=== Fáze 5: Sběr hardwarových dat a export do JSON formátu ===")
    
    # Získáme data a uložíme je do slovníku
    hw_data = get_system_data()
    
    # Zjistíme absolutní cestu pro výstupní soubor (pro uložení vedle tohoto skriptu)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    vystupni_soubor = os.path.join(dir_path, "hw_report.json")
    
    # Uložíme slovník jako soubor JSON s odsazením (indent=4) pro snadnější čtenitelnost.
    # Parametrem ensure_ascii=False dovolíme zápis znaků s diakritikou tak, aby nebyly escapovány.
    with open(vystupni_soubor, "w", encoding="utf-8") as f:
        json.dump(hw_data, f, indent=4, ensure_ascii=False)
        
    print(f"Hotovo! Detailní report byl vygenerován do souboru: {vystupni_soubor}")

# Co si z toho zapamatovat:
# - Při automatizaci chceme strojově čitelná data (JSON), ne textové výpisy z print().
# - Některé API (např. WMI) jsou vázané na jeden konkrétní OS a je třeba to v kódu zohlednit (tzv. cross-platform logika).
