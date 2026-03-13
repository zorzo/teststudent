# Fáze 1: Zobrazení objektu a jeho pozice v okně

import pygame  # Knihovna pro tvorbu 2D aplikací a her
import sys     # Systémové funkce pro korektní ukončení programu

# Inicializace všech modulů Pygame nutná před jakoukoliv prací s knihovnou
pygame.init()

# --- Nastavení okna ---
SIRKA = 600
VYSKA = 400
# Vytvoření hlavního okna, do kterého se bude vše vykreslovat
okno = pygame.display.set_mode((SIRKA, VYSKA))
pygame.display.set_caption("Souřadnicový systém - Fáze 1 (Základ)")

# --- Barvy (v RGB formátu) ---
CERNA = (0, 0, 0)       # Obvykle pro pozadí
BILA = (255, 255, 255)  # Pro texty
CERVENA = (255, 0, 0)   # Pro herní objekt (kostku)

# --- Nastavení herního objektu (kostky) ---
velikost_ctverce = 50
# Vycentrování na střed okna: střed šířky minus polovina velikosti objektu
ctverec_x = SIRKA // 2 - velikost_ctverce // 2
ctverec_y = VYSKA // 2 - velikost_ctverce // 2

# Inicializace písma pro pozdější zobrazení textu se souřadnicemi
pismo = pygame.font.SysFont("Arial", 24)

# Hodiny slouží k omezení rychlosti smyčky (FPS) a plynulejší renderování
hodiny = pygame.time.Clock()

# --- Hlavní herní smyčka ---
bezi = True
while bezi:
    # 1. Zpracování událostí (vstupy z klávesnice, myši, události oken)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Uživatel klikl na křížek pro zavření okna
            bezi = False

    # 2. Aktualizace herní logiky (v této fázi pouze statické zobrazení beze změny souřadnic)

    # 3. Vykreslování na obrazovku
    # Nejdůležitější je smazat předchozí snímek vyplněním celého okna černou barvou
    okno.fill(CERNA)
    
    # Vykreslení samotné kostky na aktuálních souřadnicích X a Y jako červený obdélník
    pygame.draw.rect(okno, CERVENA, (ctverec_x, ctverec_y, velikost_ctverce, velikost_ctverce))
    
    # Příprava a vykreslení textu s přesnými souřadnicemi do levého dolního rohu okna
    text_souradnice = f"X: {ctverec_x}, Y: {ctverec_y}"
    # render() převede textový řetězec na grafickou plochu (Surface)
    text_plocha = pismo.render(text_souradnice, True, BILA)
    # blit() umístí textovou plochu natvrdo na zadané souřadnice hlavního okna
    okno.blit(text_plocha, (10, VYSKA - 30))

    # Promítnutí všeho, co jsme do okna zatím v paměti nachystali, na fyzický displej
    pygame.display.flip()

    # Zastropení rychlosti herní smyčky na 60 snímků za vteřinu, aby to nezatěžovalo procesor
    hodiny.tick(60)

# Úplný konec aplikace po vyskočení z hlavní smyčky
pygame.quit()
sys.exit()
