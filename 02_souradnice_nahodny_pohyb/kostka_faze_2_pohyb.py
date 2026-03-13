# Fáze 2: Přidání náhodného pohybu a odrazů
import pygame # Objektová knihovna pro vývoj her a multimédií
import sys # Poskytuje přístup k proměnným a funkcím interagujících s interpretem (zde pro bezpečné ukončení)
import random # Slouží k predikovatelně náhodnému výběru počáteční rychlosti

# Inicializace Pygame
pygame.init() # Zapne a připraví všechny integrované moduly uvnitř Pygame

# Nastavení okna
SIRKA = 600 # Šířka okna v pixelech
VYSKA = 400 # Výška okna v pixelech
okno = pygame.display.set_mode((SIRKA, VYSKA)) # Aktivní instance hlavního displeje (povrchu)
pygame.display.set_caption("Souřadnicový systém - Fáze 2 (Náhodný pohyb)") # Popisek v hlavičce aplikačního okna

# Barvy (v RGB spektru)
CERNA = (0, 0, 0) # Slouží jako barva pozadí okna (vyčištění displaye)
BILA = (255, 255, 255) # Barva pro vykreslení stavového textu
CERVENA = (255, 0, 0) # Výrazná barva pro hlavní pohybující se objekt

# Nastavení objektu (čtverec)
velikost_ctverce = 50 # Strana kostky v pixelech
ctverec_x = SIRKA // 2 - velikost_ctverce // 2 # Algoritmus pro nalezení středu na ose X vzhledem k velikosti objektu
ctverec_y = VYSKA // 2 - velikost_ctverce // 2 # Algoritmus pro nalezení středu na ose Y vzhledem k velikosti objektu

# Náhodná rychlost a směr
# Vybíráme náhodnou výchylku pro každý krok (tzn. vektor rychlosti). 
# Nízké hodnoty (-2 až 2) a 0 jsme záměrně vynechali pro zajištění plynulého a svižného pohybu.
rychlost_x = random.choice([-5, -4, -3, 3, 4, 5])
rychlost_y = random.choice([-5, -4, -3, 3, 4, 5])

# Nastavení písma pro zobrazení souřadnic
pismo = pygame.font.SysFont("Arial", 24) # Výběr systémového fontu a jeho velikosti

# Hlavní smyčka
bezi = True # Hlavní flag kontrolující běh smyčky
hodiny = pygame.time.Clock() # Nástroj Pygame pro kontrolu času a snímkové frekvence

while bezi: # Nekonečná smyčka herního enginu
    # Zpracování událostí (fronta eventů)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Uživatel klikl na křížek zavření okna
            bezi = False # Flag se shodí a while cyklus bezprostředně skončí

    # Automatický pohyb přidáním konstanty rychlosti
    ctverec_x += rychlost_x # Posunutí X o daný fixní vektor v každém cyklu
    ctverec_y += rychlost_y # Posunutí Y o daný fixní vektor v každém cyklu

    # Odraz od stěn (kolizní fyzika v uzavřené krabici)
    # Detekce levé a pravé stěny - využívá matematickou disjunkci
    if ctverec_x <= 0 or ctverec_x + velikost_ctverce >= SIRKA:
        rychlost_x = -rychlost_x # Inverze vektoru vytvoří pocit fyzického odrazu směrem zpět (změna znaménka)

    # Detekce horní a dolní stěny
    if ctverec_y <= 0 or ctverec_y + velikost_ctverce >= VYSKA:
        rychlost_y = -rychlost_y # Otočí svislý směr stejným principem matematické inverze

    # Vykreslení - Pořadí je zásadní (vrstvíme jako malíř)
    okno.fill(CERNA) # Nejdřív jako první vymažeme předešlý snímek tzv. zaslepením černou barvou
    
    # Vykreslíme aktuální polohu kostky podle nových modifikovaných souřadnic
    pygame.draw.rect(okno, CERVENA, (ctverec_x, ctverec_y, velikost_ctverce, velikost_ctverce))
    
    # Příprava zobrazení souřadnic pro uživatele (Debugging overlay)
    text_souradnice = f"X: {ctverec_x}, Y: {ctverec_y}" # Formátovaný string vkládající aktuální polohu
    text_plocha = pismo.render(text_souradnice, True, BILA) # Převod fontu na pixelový povrch pro display
    okno.blit(text_plocha, (10, VYSKA - 30)) # Vykreslení textové plochy na pevně ukotvené místo obrazovky

    # Aktualizace displeje 
    pygame.display.flip() # Aplikuje vše nakreslené během tohoto cyklu na obrazovku monitoru naráz

    # Omezení FPS (Frames per second)
    hodiny.tick(60) # Umělé pozdržení cyklu tak, aby se while nevykonal více než 60x za sekundu (zamezíme plnému vytížení CPU)

# Finalizační úklid mimo "while" smyčku
pygame.quit() # Odpojí grafický modul z paměti
sys.exit() # Okamžitě ukončí bežící terminálový podproces
