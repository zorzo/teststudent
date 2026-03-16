# HW Inventura

## Popis a cíl projektu
Cílem projektu je vytvořit jednoduchou aplikaci (skript) pro detekci hardwaru (HW) a operačního systému v počítači. Program má za úkol získávat informace o systému, jako je značka a typ procesoru, kapacita RAM, informace o grafické kartě (GPU) a podobně. Aplikace je určena pro uživatele a administrátory, kteří potřebují rychle a jednoduše zjistit hardwarovou a softwarovou konfiguraci svého stroje bez nutnosti instalace dalších nástrojů.

## Funkcionalita programu
Program je tvořen skripty v jazyce Python, které postupně po fázích přistupují k systémovým informacím a vypisují je do konzole. V aktuální první fázi (`hw_inventura_01_zaklad.py`) zjistí a zobrazí název operačního systému, jeho verzi, architekturu a základní označení procesoru. 

## Technická část
- **Jazyk:** Python
- **Použité knihovny (Fáze 1):** 
  - `platform` (standardní vestavěná knihovna Pythonu sloužící k přístupu k identifikačním údajům běhového prostředí, např. OS a architektury).
- **Architektura a algoritmy:** Skript nevyužívá složité datové struktury. Spoléhá se primárně na přímé volání funkcí knihovny `platform` (jako `system()`, `release()`, `version()`, `machine()`, `processor()`). Výstupy jsou formátovány pomocí tzv. f-stringů a přímo tištěny na standardní výstup (konzole). V této fázi aplikace ke svému běhu nevyžaduje instalaci žádných externích balíčků (např. přes pip).
