"""
Fáze 6: Detailní pohled na Operační paměť (RAM) a Pevné disky
- Využívá knihovnu 'wmi', která je specifická pro Windows.
- Oproti psutil dokáže zjistit fyzické moduly RAM, jejich frekvenci, výrobce a typ.
- Detailně zobrazuje fyzické disky (nikoliv jen oddíly) včetně rozhraní a sériového čísla.
"""
import wmi

def print_ram_details(w):
    print("--- Fyzické moduly RAM ---")
    # Získáme instance třídy Win32_PhysicalMemory, která v OS Windows přímo reprezentuje fyzické moduly paměti (včetně osazení slotů)
    memory_modules = w.Win32_PhysicalMemory()
    if not memory_modules:
        print("Nepodařilo se načíst detaily o modulech paměti.")
        
    for index, module in enumerate(memory_modules):
        # Kapacita bývá v bytech, přepočteme na GB
        capacity_gb = int(module.Capacity) / (1024**3)
        print(f"Modul {index + 1}:")
        print(f"  Výrobce: {module.Manufacturer}")
        print(f"  Kapacita: {capacity_gb:.1f} GB")
        print(f"  Rychlost: {module.Speed} MHz")
        print(f"  Sériové číslo: {module.SerialNumber}")
        print(f"  Part Number: {module.PartNumber.strip()}")

def print_disk_details(w):
    print("\n--- Fyzické pevné disky ---")
    # Třída Win32_DiskDrive poskytuje data o skutečném hardwaru disků, bez ohledu na logické oddíly (C:, D: atd.)
    drives = w.Win32_DiskDrive()
    for drive in drives:
        # Velikost na GB
        size_gb = int(drive.Size) / (1024**3) if drive.Size else 0
        print(f"Disk: {drive.Model}")
        print(f"  Rozhraní: {drive.InterfaceType}")
        print(f"  Kapacita: {size_gb:.1f} GB")
        print(f"  Sériové číslo: {drive.SerialNumber.strip() if drive.SerialNumber else 'Neznámé'}")
        print(f"  Média: {drive.MediaType}")

if __name__ == "__main__":
    print("=== Fáze 6: Detailní WMI komponenty - RAM a Disky ===")
    # Následující blok zachycuje možnou chybu importu, pokud by modul wmi chyběl, 
    # a obecné výjimky při selhání komunikace s HW vnitřním systémem.
    try:
        w = wmi.WMI()
        print_ram_details(w)
        print_disk_details(w)
    except ImportError:
        print("Knihovna wmi není nainstalována. Před spuštěním proveďte: pip install wmi")
    except Exception as e:
        print(f"Obecná chyba při inicializaci WMI: {e}")

# Co si z toho zapamatovat:
# - Rozhraní WMI (Windows Management Instrumentation) je zlatý důl pro skriptování na Windows.
# - Win32_PhysicalMemory poskytuje data přímo ze základní desky, takže vidíme rozložení modulů ve slotech.
# - Win32_DiskDrive vrací data o samotném železe disku (nebereme v potaz dělení disku na logické disky C:, D:).
