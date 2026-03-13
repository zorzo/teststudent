# Kostka v souřadnicovém systému

## Popis a cíl projektu
Projekt je zaměřen na demonstraci práce dvousměrného (2D) souřadnicového systému v programovacím jazyce Python za použití knihovny Pygame. Cílem je naučit se vykreslovat objekty, sledovat jejich souřadnice v prostoru a tyto údaje zobrazovat vizuálně na obrazovce. Ve 2. fázi simulujeme neustálý pohyb kostky s automatickým vyhodnocováním kolizí s okraji (odrážení od stěn). Aplikace je určena začátečníkům k pochopení zobrazovacího systému a vizualizace matematických souřadnic v pohybu.

## Funkcionalita programu
Aktuální verze programu se skládá z následujících prvků:
- Inicializace a nastavení hlavního pracovního okna pevné šířky a výšky.
- Vykreslení barevného objektu (kostky), který je při spuštění vycentrován a obdrží náhodný počáteční vektor rychlosti pohybu.
- Automatický pohyb objektu a odrážení se od okrajů okna pomocí matematické inverze rychlosti (`rychlost = -rychlost`).
- Živé (real-time) zobrazení aktuálních souřadnic (X a Y) vykreslením textu přímo do okna.
- Zajištění chodu programu pomocí hlavní herní smyčky ošetřené proti "zamrznutí" a udržující pevnou frekvenci (tzv. FPS cap).

## Technická část
- **Použité knihovny:** `pygame` (grafický modul pro vykreslování a obsluhu událostí), `sys` (pro korektní celkové ukončení procesu skriptu), `random` (pro generování náhodného směru a rychlosti na počátku).
- **Logika algoritmu:** K vycentrování pozice se využívá výpočet přes celočíselné dělení. Pro směr pohybu se volí náhodně vektor rychlosti na ose X a Y tak, aby nebyl nulový nebo příliš pomalý. Pokud souřadnice + rozměr objektu přesáhne okraj obrazovky (0 nebo MAXIMUM), dojde k reverzi směru. 
- **Datové struktury:** Pro uchování definic částí barev a obdélníkových rozměrů se využívají základní datové typy tuple `(R, G, B)` a proměnné celočíselného typu. Odrazy využívají logické spojky `or`.
