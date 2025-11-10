'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81          # m/s² – tíhové zrychlení na Zemi
MOON_GRAVITY = 1.62           # m/s² – tíhové zrychlení na Měsíci
SPEED_OF_LIGHT = 299_792_458  # m/s – rychlost světla ve vakuu
SPEED_OF_SOUND = 343          # m/s – rychlost zvuku při 20 °C v suchém vzduchu
''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
''



def weight_on_earth(mass):

    return mass * EARTH_GRAVITY

def weight_on_moon(mass):
  "
    return mass * MOON_GRAVITY

def light_travel_time(distance):
    
    return distance / SPEED_OF_LIGHT

def sound_travel_time(distance):
   
    return distance / SPEED_OF_SOUND
