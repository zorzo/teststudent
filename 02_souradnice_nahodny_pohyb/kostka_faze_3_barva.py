# Fáze 3: Přidání změny barvy, pulzování a částicového efektu (Particle System)
import pygame
import sys
import random

# Inicializace interních softwarových modulů Pygame do paměti
pygame.init()

# Nastavení logické architektury herního okna
SIRKA = 600
VYSKA = 400
okno = pygame.display.set_mode((SIRKA, VYSKA)) # Aktivní vizuální interface enginu
pygame.display.set_caption("Souřadnicový systém - Fáze 3 (Pulzování a částice)")

# Barvy aplikované na abstraktní vrstvy
CERNA = (0, 0, 0) # Slouží jako čistící background (pozadí)
BILA = (255, 255, 255) # Použito pro textový HUD (Heading-Up Display) overlay

# Nastavení struktury primárního objektu (kostky)
zakladni_velikost = 50 # Základní referenční bod (Baseline) pro výpočty kolizí
velikost_ctverce = zakladni_velikost # Modifikovatelná (Live) velikost v animaci pulzu
ctverec_x = SIRKA // 2 - zakladni_velikost // 2
ctverec_y = VYSKA // 2 - zakladni_velikost // 2

# Instanční proměnné pro algoritmus pulzování velikosti (tzv. "dýchání")
pulz_smer = 1 # Směr modifikátoru (Kladně = akcelerace zvětšování)
pulz_rychlost = 0.5 # Míra posunu velikosti pro každý cyklus smyčky
pulz_min = 40 # Limitní minimální bod (spodek amplitudy komprese)
pulz_max = 60 # Limitní maximální bod (vrchol amplitudy expanze)

# Systém rotujících barev s podporou zjednodušeného HSL barveného prostoru
aktualni_hue = random.randint(0, 359) # Náhodný bod barevného RGB kola
barva_objekt = pygame.Color(0, 0, 0) # Inicializace specializované třídy pygame pro dynamickou barvu
# Aplikace Hue do HSLA indexu (odstín z proměnné, sytost na 100%, světlost na 50%, alfa kanál 100%)
barva_objekt.hsla = (aktualni_hue, 100, 50, 100) 
aktualni_barva = (barva_objekt.r, barva_objekt.g, barva_objekt.b) # Extrakt převodu zpět do formátu Tuple přes RGB pro vykreslovač

# Počáteční vektor rychlosti tělesa v rovině (vyloučeny pomalé rychlosti 0 až 2)
rychlost_x = random.choice([-5, -4, -3, 3, 4, 5])
rychlost_y = random.choice([-5, -4, -3, 3, 4, 5])

# Architektura částicového efektu po srážkách (Particle Engine)
# Kolekce (List) pro záznam živých entit sutě. Každý bod uvnitř pole bude reprezentován zapouzdřeným Slovníkem (Dict).
castice = [] 

# Objekty pre-renderovaných fontů pro HUD
pismo = pygame.font.SysFont("Arial", 24)

# Základní proměnné životního cyklu programu
bezi = True
hodiny = pygame.time.Clock() # Řízení reálného časovače z CPU (Frame regulátor)

while bezi: # Nekonečná smyčka
    aktualni_cas = pygame.time.get_ticks() # Dotaz do enginu na uplynulý počet milisekund od startu (časostop zrodu programu)

    # Zachytávání událostí OS a uživatele do eventové fronty
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bezi = False # Programová destrukce while cyklu při zavření okna

    # Matematický zápis pro integraci fixního posunu objektu prostorem
    ctverec_x += rychlost_x
    ctverec_y += rychlost_y

    # Vizuální deformační efekt pulzování
    velikost_ctverce += pulz_smer * pulz_rychlost # Aplikace stupnice expanze/komprese
    # Kontrola intervalů: Pokud objekt dosáhne stanovených maxim/minim, reverzneme modifikátor a otočíme jeho chování
    if velikost_ctverce >= pulz_max or velikost_ctverce <= pulz_min:
        pulz_smer *= -1

    # Animace barveného spektra tělesa
    # Modulo 360 hlídá, že hodnota po sčítání inkrementů bezchybně přeteče ihned z "359" zpět na start do "0"
    aktualni_hue = (aktualni_hue + 1) % 360
    barva_objekt.hsla = (aktualni_hue, 100, 50, 100) # Re-implementace dynamické barvy s novým Hue Indexem
    aktualni_barva = (barva_objekt.r, barva_objekt.g, barva_objekt.b)

    naraz = False # Trigger vlaječka pro Particle engine detekující kolize na krajích aplikace

    # Výpočet detekce okrajů (Bouncing engine s pevnou základní hranicí pevné kostky pro prevenci chyb)
    # Detekce levé a pravé stěny skrze limitní hodnoty oken (+/- 0)
    if ctverec_x <= 0 or ctverec_x + zakladni_velikost >= SIRKA:
        rychlost_x = -rychlost_x # Těžištěm inverze na vektoru (inverzní rychlost logicky posune tah zpět proti nárazu)
        # Ošetření problému "zaseknutí se do mantinelu": vycentruje prvek striktně zpět do legalizovaných limitů povolené souřadnice 
        ctverec_x = max(0, min(ctverec_x, SIRKA - zakladni_velikost))
        naraz = True # Odpálení signálu pro emitory částic

    # Zrcadlově identický engine detekce svislé osy (Dolní a horní limity oken proti výšce a spodní vrstvě 0)
    if ctverec_y <= 0 or ctverec_y + zakladni_velikost >= VYSKA:
        rychlost_y = -rychlost_y
        ctverec_y = max(0, min(ctverec_y, VYSKA - zakladni_velikost))
        naraz = True

    # Generátor Particle enginu: Vystřelení úlomků při události nárazu s krajem okna
    if naraz:
        aktualni_hue = random.randint(0, 359) # Jumpscare skoková modulace na zcela odlišnou barvu z RGB barevného kola
        
        # Emise a alokace mezi 5 a 7 novými entitami letící roztříštěné sutě 
        pocet_castic = random.randint(5, 7)
        for _ in range(pocet_castic): # Používáme underscore (_), k paměťové adrese čítače cyklu se už dál nevracíme 
            # Vstřik generované částice coby komplexního datového slovníku do živé fronty Pole (Listu) vyrenderovaných objektů
            castice.append({
                'x': ctverec_x + zakladni_velikost / 2, # Vycentrování spawn pointu ze středu mateřského tělíska
                'y': ctverec_y + zakladni_velikost / 2,
                'vx': random.uniform(-6, 6) + rychlost_x * 0.5, # Tříštivý vektor letu posilovaný původní kinetickou energií kostky s ohledem na osu letu X v okamžiku nárazu
                'vy': random.uniform(-6, 6) + rychlost_y * 0.5, # Totéž pro směr OS Y (vertikální částice)
                'barva': (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)), # Unikátní RGB kód poskládaný pro každý individuální odštěpek
                'cas_vzniku': aktualni_cas # Timestamp jako razítko pro pozdější detekci stáří fragmentu a její programovou terminaci
            })

    # Fáze vykreslování herního pole do mezipaměti
    okno.fill(CERNA) # Vymazání (zalití) backgroundu pro potlačení starých snímků z předešlých loopů
    
    # Práce Memory Manageru zaměřená na filtraci mrtvých (příliš starých) úlomků fragmentů
    nove_castice = [] # Dočasný list určený sběru přeživších (alokace pro bezpečný bypass cyklu)
    for c in castice:
        # Time to live algoritmus (TTL): Porovnávám procesingový čas z úvodu cyklu a timestamp pořízení sutě, jestli fragment žije do 700 ms (0.7 s)
        if aktualni_cas - c['cas_vzniku'] < 700:
            c['x'] += c['vx'] # Vnitřní animace dynamického rozstřiku prachového kusu
            c['y'] += c['vy']
            velikost_c = 8 # Pevně limitovaná výseč střepiny v pixelech
            pygame.draw.rect(okno, c['barva'], (c['x'] - velikost_c/2, c['y'] - velikost_c/2, velikost_c, velikost_c)) # Zakreslení fyzického projevu proměnných slovníku (barva a poloha) do pixelu Memory okna
            nove_castice.append(c) # Tedy entita dožije s přehledem i další exekuci
            
    castice = nove_castice # Bezpečné nahrazení (Overrullnutí) starého Listu fragmentů seznamem jen těch aktuálně relevantních "tepajících" prvků, staré tak Garbage Collector zahodí  

    # Rekonstrukci centrálního těžiště mateřské kostky z důvodu "rozlezení" při pulzování modifikátorem velikosti 
    # Vypočteme, kolik bodů stran se odtrhne do krajin a zkompenzujeme s fixním středem
    odsazeni = (zakladni_velikost - velikost_ctverce) / 2
    vykreslit_x = ctverec_x + odsazeni
    vykreslit_y = ctverec_y + odsazeni
    
    # Finální zápis dynamicky vyvíjejícího se objemu a bravy objektu
    pygame.draw.rect(okno, aktualni_barva, (vykreslit_x, vykreslit_y, velikost_ctverce, velikost_ctverce))
    
    # Příprava výkresu informačního HUD bloku  - (Pozice fixována vždy na pevnou základní souřadnici matky z počátku inicializace)
    text_souradnice = f"X: {int(ctverec_x)}, Y: {int(ctverec_y)}" # Nástroj int() slouží k promazání chaotických dlouhých float hodnot s desetiným ocasem pro čistotu terminálu
    text_plocha = pismo.render(text_souradnice, True, BILA) # Skalární proces renderovaní fontu a převedení stringu pro Pixelové zobrazení v okně 
    okno.blit(text_plocha, (10, VYSKA - 30)) # Zápis na absolutní pozici (Dolní levý spodní roh okna)

    pygame.display.flip() # Swap Buffer prohodí námi naskládanou vrstvu z paměti a nahradí jíž finálně výrez na LCD z důvodu plynulosti herního běhu

    # Frame lock limitator
    hodiny.tick(60) # Nedovolí systému utrhnout se ze řetězu, zabraňuje stoupnutí exekucí enginu Python přes 60 loppů za sekundu. 

# De-lokace modulu pro finální úklid paměti na HW vrstvě po QUIT evokaci
pygame.quit()
sys.exit() # Systémový bypass shozen
