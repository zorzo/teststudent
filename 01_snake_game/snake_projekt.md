# Dokumentace ke hře Snake (snake_game/snake10_2.py)

## O projektu
Tento projekt je fází vývoje hry Snake (Had) pomocí knihovny **Pygame** v jazyce Python.
V této fázi (`snake10_2.py`) je implementováno herní okno, vykreslení hada (jako jeden čtverec) a jídla na náhodných pozicích.

## Požadavky
Pro spuštění hry je nutné mít nainstalovaný Python a knihovnu Pygame.

1.  **Python** (verze 3.x)
2.  **Pygame**

Instalace knihovny Pygame pomocí pip:
```bash
pip install pygame
```

## Popis kódu

Skript `snake10_2.py` obsahuje inicializaci, herní objekty a hlavní smyčku pro vykreslování.

### Hlavní konstanty a nastavení:
- `OKNO`: Velikost herního okna nastavena na **1000x1000** pixelů.
- `TILE_SIZE`: Velikost jednoho políčka (dlaždice) je **30** pixelů. (Had a jídlo mají velikost o 2 pixely menší pro okraj).
- `RANGE`: Rozsah souřadnic pro generování náhodných pozic tak, aby objekty zůstaly v okně.

### Hlavní součásti:

1.  **Import knihoven**:
    - `pygame as pg`: Hlavní knihovna pro grafiku a herní smyčku.
    - `random`: Pro generování náhodných pozic jídla a hada.
    - `sys`: Pro korektní ukončení programu.

2.  **Herní objekty**:
    - **Snake**: Objekt `pg.Rect` reprezentující hada. Začíná na náhodné pozici.
    - **Food**: Objekt `pg.Rect` reprezentující jídlo. Je kopií hada, ale na jiné náhodné pozici.
    - `get_random_position`: Lambda funkce pro generování souřadnic v rámci mřížky.

3.  **Hlavní smyčka (Game Loop)**:
    - **Event Handling**: Sleduje událost `pg.QUIT` pro zavření okna.
    - **Vykreslování**:
        - Obrazovka se maže černou barvou (`screen.fill('black')`).
        - **Jídlo** se vykresluje červeně.
        - **Had** se vykresluje zeleně.
    - **Update**: `pg.display.flip()` aktualizuje obsah okna.
    - **FPS**: `clock.tick(60)` omezuje běh na 60 snímků za sekundu.

## Spuštění
Skript lze spustit z příkazové řádky:
```bash
python snake_game/snake10_2.py
```
Po spuštění se otevře černé okno o rozměrech 1000x1000 pixelů, kde se zobrazí zelený čtverec (had) a červený čtverec (jídlo).
