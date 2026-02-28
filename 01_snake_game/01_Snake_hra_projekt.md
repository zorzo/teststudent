# Hra Snake

## Popis a cíl projektu
Cílem tohoto projektu je vytvořit klasickou hru "Had" (Snake) v jazyce Python s využitím knihovny **Pygame**. Hra je vyvíjena postupně v několika fázích. Aktuální fáze (`snake10_5.py`) doplňuje plnou logiku hry – kromě ovládání pohybu přidává generování potravy a zvětšování hada při pojídání.
Aplikace je určena pro začínající programátory jako ukázka práce s grafikou, událostmi a časováním v herním enginu.

## Funkcionalita programu
Program se skládá z následujících technických prvků:

1.  **Grafické okno**: Vytvořeno pomocí `pg.display.set_mode`. Velikost je nastavitelná (aktuálně 1000x1000 px).
2.  **Reprezentace objektů**: Had (hlava) i jídlo jsou definovány jako objekty `pg.Rect`, což usnadňuje detekci kolizí metodou `colliderect` a vykreslování. Hadovo tělo je pole (seznam) částí kopírující tvar hlavy.
3.  **Algoritmus pohybu a kolizí**:
    - Pohyb je řešen pomocí vektoru `snake_dir`, který se mění na základě stisku kláves (šipky).
    - Aby se had nepohyboval příliš rychle (při každém průchodu smyčkou), je implementován časovač (`pg.time.get_ticks()`). Had se pohne pouze po uplynutí intervalu `time_step` (250 ms).
    - Zvětšování a udržování délky se opírá o ořezávání listu z jeho konce – přidá se nová hlava dopředu a pokud had nic nesnědl, odebere se konec. Délka stoupá po kolizi s jídlem.
4.  **Generování pozic**: Využívá knihovnu `random` a anonymní `lambda` funkci pro umístění objektů do mřížky odpovídající velikosti políček (`TILE_SIZE`).

### Technická část
Kód je rozdělen na inicializační část (nastavení konstant, objektů a okna) a hlavní nekonečnou smyčku (Game Loop). S využitím těchto závislostí:
- **Python 3.x**: Základní programovací jazyk.
- **Pygame**: Knihovna pro tvorbu her (vykreslování, správa událostí, časování).
- **Random**: Pro náhodné generování pozic jídla.

## Technický popis struktury
Smyčka v každém kroku:
1.  Kontroluje vstupy z klávesnice.
2.  Maže obrazovku.
3.  Vykresluje objekty.
4.  Provádí logiku posunu podle času.
5.  Aktualizuje zobrazení.

### Instalace a spuštění
1.  Ujistěte se, že máte nainstalovaný Python 3.
2.  Nainstalujte knihovnu Pygame: `pip install pygame`.
3.  Spusťte finální skript: `python 01_snake_game/snake10_5.py`.
