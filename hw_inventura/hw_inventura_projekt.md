# HW Inventura

## Popis a cíl projektu
Cílem projektu je vytvořit jednoduchou aplikaci (skript) pro detekci hardwaru (HW) a operačního systému v počítači. Program má za úkol získávat informace o systému, jako je značka a typ procesoru, kapacita RAM, informace o grafické kartě (GPU) a podobně. Aplikace je určena pro uživatele a administrátory, kteří potřebují rychle a jednoduše zjistit hardwarovou a softwarovou konfiguraci svého stroje bez nutnosti instalace dalších nástrojů.

## Funkcionalita programu
Program je tvořen skripty v jazyce Python, které postupně po fázích přistupují k systémovým informacím a vypisují je do konzole:
- **Fáze 1 (`hw_inventura_01_zaklad.py`):** Zjistí a zobrazí název operačního systému, jeho verzi, architekturu a základní označení procesoru bez nutnosti instalovat externí knihovny.
- **Fáze 2 (`hw_inventura_02_pamet_disky.py`):** Dále zjišťuje podrobnější informace o CPU (počet fyzických i logických jader), počítá celkovou kapacitu operační paměti (RAM) v gigabytech a vypisuje přehled pevných disků (včetně typu souborového systému a bodu připojení).
- **Fáze 3 (`hw_inventura_03_funkce.py`):** Přináší detailnější a přesnější čitelný identifikátor procesoru včetně jeho základní frekvence. Kód je nově strukturován a refaktorován do znovupoužitelných funkcí.
- **Fáze 4 (`hw_inventura_04_gpu_chyby.py`):** Slouží k detekci dedikovaných grafických karet (primárně NVIDIA) a zobrazuje jejich celkovou VRAM paměť a aktuální teplotu. Celý proces je ošetřen pro případ selhání načítání dat.
- **Fáze 5 (`hw_inventura_05_kompletni_json.py`):** Představuje komplexní inventuru (s ohledem na operační systém Windows) a umožňuje hromadný export nasbíraných dat do formátu JSON (datového slovníku). Namísto prostého výpisu do konzole se data ukládají do souboru `hw_report.json` pro další případné zpracování.

## Technická část
- **Jazyk:** Python
- **Použité knihovny:** 
  - `platform` (standardní vestavěná knihovna Pythonu sloužící k přístupu k identifikačním údajům běhového prostředí, např. OS a architektury).
  - `psutil` (externí knihovna pro získání informací o využití systému – CPU, paměť, disky). Vyžaduje instalaci pomocí správce balíčků (`pip install psutil`).
  - `py-cpuinfo` (externí knihovna pro získání detailních a přesných názvů CPU a jejich parametrů). Vyžaduje instalaci přes správce balíčků (`pip install py-cpuinfo`).
  - `gputil` (externí knihovna pro zjišťování stavu grafických karet). Vyžaduje instalaci (`pip install gputil`).
  - `json` (standardní vestavěná knihovna pro zápis a čtení formátu JSON, použitá pro export ve fázi 5).
  - `wmi` (externí knihovna umožňující detailní dotazování na hardware s využitím Windows Management Instrumentation na platformě Windows).
- **Architektura a algoritmy:** Během prvních fází se skripty spoléhaly primárně na přímé volání funkcí knihoven z hlavního bloku a formátování f-stringy. Od fáze 3 je kód strukturován a logicky členěn **do znovupoužitelných funkcí** (např. `get_os_info()`, `get_cpu_info()`), což zvyšuje čitelnost a udržovatelnost kódu. Skript chrání čtení proměnných z externího API slovníků bezpečným voláním přes metodu `.get()` (předcházení pádům skriptu při chybějících hodnotách). Ke komunikaci s hardwarem (speciálně od fáze 4 a 5) skript extenzivně využívá bloky `try-except`, které rozeznávají problémy se systémovým voláním (například chybějící knihovna nebo neschopnost knihovny komunikovat s daným fyzickým zařízením). Díky tomu aplikace ihned nespadne, ale zpracování ostatních komponent pokračuje. Celkový výsledek je ukládán do slovníku asymetrické struktury a posléze plně serializován do formátu JSON.
