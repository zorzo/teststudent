# HW Inventura

## Popis a cíl projektu
Cílem projektu je vytvořit jednoduchou aplikaci (skript) pro detekci hardwaru (HW) a operačního systému v počítači. Program má za úkol získávat informace o systému, jako je značka a typ procesoru, kapacita RAM, informace o grafické kartě (GPU) a podobně. Aplikace je určena pro uživatele a administrátory, kteří potřebují rychle a jednoduše zjistit hardwarovou a softwarovou konfiguraci svého stroje bez nutnosti instalace dalších nástrojů.

## Funkcionalita programu
Program je tvořen skripty v jazyce Python, které postupně po fázích přistupují k systémovým informacím a vypisují je do konzole:
- **Fáze 1 (`hw_inventura_01_zaklad.py`):** Zjistí a zobrazí název operačního systému, jeho verzi, architekturu a základní označení procesoru bez nutnosti instalovat externí knihovny.
- **Fáze 2 (`hw_inventura_02_pamet_disky.py`):** Dále zjišťuje podrobnější informace o CPU (počet fyzických i logických jader), počítá celkovou kapacitu operační paměti (RAM) v gigabytech a vypisuje přehled pevných disků (včetně typu souborového systému a bodu připojení).

## Technická část
- **Jazyk:** Python
- **Použité knihovny:** 
  - `platform` (standardní vestavěná knihovna Pythonu sloužící k přístupu k identifikačním údajům běhového prostředí, např. OS a architektury).
  - `psutil` (externí knihovna pro získání informací o využití systému – CPU, paměť, disky). Vyžaduje instalaci pomocí správce balíčků (`pip install psutil`).
- **Architektura a algoritmy:** Skripty se spoléhají primárně na přímé volání funkcí z knihoven `platform` a `psutil` (např. `cpu_count()`, `virtual_memory()`, `disk_partitions()`). Pro zobrazení srozumitelných hodnot využívají operátory k převodu bytů na gigabyty a pro výpis disků využívají cyklus `for`. Výstupy jsou formátovány pomocí f-stringů a tištěny do konzole.
