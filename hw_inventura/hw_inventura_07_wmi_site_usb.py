"""
Fáze 7: Sítě, MAC adresy a detekce připojených USB zařízení
- Pomocí WMI zkoumáme aktivní síťové adaptéry.
- Procházíme seznam USB řadičů a hubů (pro zjištění, co vše je k PC připojeno).
"""
import wmi

def get_network_adapters(w):
    """
    Získá seznam aktivních síťových adaptérů vázaných na IP adresu.
    K třídě Win32_NetworkAdapterConfiguration se dotazuje pomocí parametru IPEnabled=True.
    Tím skript efektivně odfiltruje různé virtuální, odpojené či Bluetooth adaptéry 
    a vrátí jen ty, které mají systémovou IP konfiguraci.
    """
    print("--- Aktivní síťové adaptéry ---")
    # Provedení dotazu na WMI s filtrem (zachycení jen aktivních/používaných síťových připojení)
    adapters = w.Win32_NetworkAdapterConfiguration(IPEnabled=True)
    
    if not adapters:
        print("Nebyl nalezen žádný aktivní síťový adaptér s IP adresou.")

    # Procházení kolekce nalezených adaptérů a tisk detailních informací
    for net in adapters:
        # MACAddress a Description jsou řetězce (string), zatímco IPAddress je často pole (seznam/tuple)
        print(f"Adaptér: {net.Description}")
        print(f"  MAC Adresa: {net.MACAddress}")
        # Většina adaptérů může mít více IP (IPv4 i IPv6), skript vezme první ze seznamu (zpravidla IPv4)
        print(f"  IP Adresa: {net.IPAddress[0] if net.IPAddress else 'Nenastavena'}")
        
        # Hodiota DHCPEnabled představuje boolean (True/False)
        print(f"  DHCP Povoleno: {'Ano' if net.DHCPEnabled else 'Ne'}")
        print("-" * 20)

def get_usb_controllers(w):
    """
    Získá a vypíše strukturu USB řadičů pomocí WMI. 
    Třída Win32_USBController slouží k jednoduchému výpisu základních deskových i externích řadičů a hubů zajišťujících provoz přes USB rozhraní.
    """
    print("\n--- USB Řadiče ---")
    # Tento sběr dává surové údaje o HW modulech - pro detekci např. zapojené flashky by byl použit Win32_DiskDrive
    usb_controllers = w.Win32_USBController()
    
    # Práce s vestavěnou funkcí enumerate poskytne automatické číslování ve výpisu
    # Začátek smyčky mapuje každý controller do objektu a získá 'Name' (Název) a 'Manufacturer' (Výrobce)
    for index, usb in enumerate(usb_controllers):
        print(f"{index + 1}. {usb.Name} (Výrobce: {usb.Manufacturer})")

if __name__ == "__main__":
    print("=== Fáze 7: Sítě a USB přes WMI ===")
    try:
        w = wmi.WMI()
        get_network_adapters(w)
        get_usb_controllers(w)
    except Exception as e:
        print(f"Došlo k chybě: {e}")

# Co si z toho zapamatovat:
# - Většina PC má mnoho virtuálních síťových adaptérů (Bluetooth, VPN). Filtrování přes 'IPEnabled=True' odhalí ty aktuálně používané.
# - S WMI můžete vytvořit skript, který detekuje vložený USB disk, nebo naopak určitá USB zablokuje změnou registru.
