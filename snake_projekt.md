# Dokumentace ke hře Snake (snake.py)

## O projektu
Tento projekt je jednoduchá implementace klasické hry Snake (Had) pomocí knihovny **Pygame** v jazyce Python.

## Požadavky
Pro spuštění hry je nutné mít nainstalovaný Python a knihovnu Pygame.

1.  **Python** (verze 3.x)
2.  **Pygame**

Instalace knihovny Pygame pomocí pip:
```bash
pip install pygame
```

## Popis kódu

Skript `snake.py` momentálně obsahuje základní inicializaci herního okna.

### Hlavní součásti:

1.  **Import knihoven**:
    - `pygame`: Hlavní knihovna pro tvorbu her.
    - `random`: Knihovna pro generování náhodných čísel (připravena pro budoucí použití, např. pro generování jídla).

2.  **Inicializace Pygame**:
    - `pygame.init()`: Inicializuje všechny moduly Pygame.

3.  **Nastavení okna**:
    - `window_width`: Šířka okna nastavena na 800 pixelů.
    - `window_height`: Výška okna nastavena na 600 pixelů.
    - `pygame.display.set_mode()`: Vytvoří okno o zadaných rozměrech.
    - `pygame.display.set_caption()`: Nastaví titulek okna na "Snake Game".

## Spuštění
Skript lze spustit z příkazové řádky:
```bash
python snake.py
```
Po spuštění se otevře herní okno o rozměrech 800x600 pixelů.
