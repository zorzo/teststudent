import time
import datetime
import subprocess
import sys

# Nastavení cílového data a času 
cilovy_cas = datetime.datetime(2026, 3, 19, 8, 55, 0)

def proved_git_tydenni_update():
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Spouštím odesílání na GitHub...")
    
    try:
        # Přidání všech změněných souborů do stage
        subprocess.run(["git", "add", "."], check=True)
        
        # Vytvoření commitu. Zpráva by měla odpovídat pravidlům pro AI hodnocení (např. trpný/minulý čas)
        zprava_commitu = "Přidána fáze 6 HW Inventury: detaily RAM a disků přes WMI"

        subprocess.run(["git", "commit", "-m", zprava_commitu], check=True)
        
        # Odeslání (push) na vzdálený server
        subprocess.run(["git", "push"], check=True)
        print("✅ Hotovo! Kód byl úspěšně odeslán na GitHub.")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Nastala chyba při odesílání na GitHub: {e}")

def main():
    nyni = datetime.datetime.now()
    
    if nyni >= cilovy_cas:
        print("Cílový čas už vypršel! Odesílám okamžitě...")
        proved_git_tydenni_update()
        sys.exit()
    
    # Výpočet, kolik sekund zbývá do cílového času
    zbyva_sekund = (cilovy_cas - nyni).total_seconds()
    
    hodiny, zbytek = divmod(zbyva_sekund, 3600)
    minuty, sekundy = divmod(zbytek, 60)
    
    print(f"Automatické odeslání je nastaveno na: {cilovy_cas.strftime('%d.%m.%Y %H:%M:%S')}")
    print(f"Skript nyní bude čekat: {int(hodiny)} hodin, {int(minuty)} minut a {int(sekundy)} sekund.")
    print("NEZAVÍREJTE TOTO OKNO! ☕")
    
    # Uspání programu do zadaného času
    time.sleep(zbyva_sekund)
    
    # Spuštění odesílací funkce
    proved_git_tydenni_update()

if __name__ == "__main__":
    main()
