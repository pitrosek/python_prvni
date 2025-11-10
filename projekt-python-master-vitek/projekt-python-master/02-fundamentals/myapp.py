import physics

hmotnost = 70      
vzdalenost = 1000  

print("Hmotnost:", hmotnost, "kg")
print("Váha na Zemi:", physics.weight_on_earth(hmotnost), "N")
print("Váha na Měsíci:", physics.weight_on_moon(hmotnost), "N")
print("Čas, za který světlo urazí 1 km:", physics.light_travel_time(vzdalenost), "s")
print("Čas, za který zvuk urazí 1 km:", physics.sound_travel_time(vzdalenost), "s")
