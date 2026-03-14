# Kostka v souřadnicovém systému

## Popis a cíl projektu
Projekt je zaměřen na demonstraci práce dvousměrného (2D) souřadnicového systému v programovacím jazyce Python za použití knihovny Pygame. Ve 3. fázi rozšiřuje předchozí pohybový engine o vizuální a částicové (particle) efekty. Cílem je představit pokročilejší chování kostky – simulaci dýchání formou pulzování barev (v barevném prostoru HSLA) a plynulé změny rozměru z vlastního středu. Dále implementuje efektní zrození částicového systému při detekci kolize s okrajem obrazovky. Aplikace prohlubuje znalosti vizualizace dat v animaci a rozšiřuje vhled do sofistikovanějších algoritmů.

## Funkcionalita programu
Aktuální verze programu nabízí následující prvky a vizuální inovace:
- Inicializace a nastavení hlavního pracovního okna pevné šířky a výšky.
- Vykreslení objektu, který navíc aplikuje dynamickou rotaci barev (plynulá změna Hue ze spektra HSV/HSL) na svém zevnějšku.
- Algoritmus pulzování velikosti (tzv. "dýchání") objektu z jeho geometrického středu, kde se pravidelně zvětšuje a zmenšuje v pevně stanovených mezích.
- Automatický pohyb objektu a matematické odrážení se od okrajů okna s preventivním ošetřením "zaseknutí se do mantinelu".
- Generování částicového efektu na místě srážky: vyvržení několika drobných fragmentů, které se následně po krátkém časovém limitu destrukčně odstraní z pole pro vykreslování.
- Živé (real-time) zobrazení aktuálních souřadnic (X a Y) vykreslením upraveného (čitelnější ho zkráceného) textu na fixní místo okna.

## Technická část
- **Použité knihovny:** `pygame` (grafický modul obsluhující okno, animaci barev přes třídu `Color` a systémový čas skrze `get_ticks`), `sys` (ukončení), `random` (pro generování počáteční rychlosti i náhodného rozmezí rychlostí a barev částic).
- **Logika algoritmu:** Plynulá oscilace barvy je aplikována skrze zvyšování `(hue + 1) % 360` a transformována objektem `pygame.Color`. U velikosti se kontrolují meze expanze/komprese a inverzním způsobem se násobí index směru pulzu. Kompenzací přes odsazení se zjišťuje nový výpočtový střed pro vykreslení pozměněné struktury kostky.
- **Datové struktury:** Pro uchování nezávisle definovaných částic z efektu kolize je využita struktura jednorozměrného pole (`list`), v níž je uchováván navázaný slovník (`dict`). Ve slovníku má každá částice zaznamenané unikátní vektory letu, vlastní barvu a systémový "časostop zrodu", pomocí kterého engine určí konec její životnosti smazáním z pole částic.
