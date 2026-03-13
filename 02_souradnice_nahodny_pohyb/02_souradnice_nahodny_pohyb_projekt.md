# Kostka v souřadnicovém systému

## Popis a cíl projektu
Projekt je zaměřen na demonstraci práce dvousměrného (2D) souřadnicového systému v programovacím jazyce Python za použití knihovny Pygame. Cílem je naučit se vykreslovat objekty, sledovat jejich souřadnice v prostoru a tyto údaje zobrazovat vizuálně na obrazovce. Jedná se o základ, na kterém budou stavěny další, složitější funkce (pohyb, srážky atd.). Aplikace je určena začátečníkům k pochopení zobrazovacího systému a vizualizace matematických souřadnic.

## Funkcionalita programu
Aktuální verze programu se skládá z následujících prvků:
- Inicializace a nastavení hlavního pracovního okna pevné šířky a výšky.
- Vykreslení barevného statického objektu (kostky), který je při spuštění vycentrován.
- Živé (real-time) zobrazení aktuálních souřadnic (X a Y) vykreslením textu přímo do okna.
- Zajištění chodu programu pomocí hlavní herní smyčky ošetřené proti "zamrznutí" a udržující pevnou frekvenci (tzv. FPS cap).

## Technická část
- **Použité knihovny:** `pygame` (grafický modul pro vykreslování a obsluhu událostí), `sys` (pro korektní celkové ukončení procesu skriptu).
- **Logika algoritmu:** K vycentrování pozice se využívá výpočet přes celočíselné dělení `SIRKA // 2 - velikost_objektu // 2`. Kód je sestaven jako nekonečná herní smyčka spravovaná vestavěným objektem událostí.
- **Datové struktury:** Pro uchování definic částí barev a obdélníkových rozměrů se využívají základní datové typy tuple `(R, G, B)` a proměnné celočíselného typu.

