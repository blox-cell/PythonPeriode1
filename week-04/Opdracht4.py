## Opdracht - Weapon Selector
#
# Je gaat een programma maken waarin een speler een wapen kan kiezen.
# Ieder wapen heeft zijn eigen damage en een speciale eigenschap.
#
# Stap 1 - Variabelen
# Maak de volgende variabelen aan:
# - Een variabele voor de naam van de speler
# - Een variabele voor het gekozen wapen
# - Een variabele voor de damage van het wapen
#
# Geef de speler zelf een naam en kies alvast een wapen.
#
# LET OP:
# Gebruik voor alle variabelen de juiste Python naming conventions!
# Bijvoorbeeld: player_name in plaats van playerName.

# Stap 1 code:
player_name = "Steve"
selected_weapon = "Sword"
weapon_damage = 0


# Stap 2 - Match Case
# Gebruik een match case om te controleren welk wapen de speler heeft.
#
# De speler kan kiezen uit de volgende wapens:
#
# Sword:
# - Doet 20 damage
# - Print "Je gebruikt een zwaard!"
#
# Bow:
# - Doet 15 damage
# - Print "Je gebruikt een boog!"
#
# Staff:
# - Doet 25 damage
# - Print "Je gebruikt een magische staf!"
#
# Axe:
# - Doet 30 damage
# - Print "Je gebruikt een bijl!"
#
# Zorg ervoor dat de damage variabele de juiste waarde krijgt.
#
# Als de speler een onbekend wapen heeft gekozen:
# - Zet de damage op 0
# - Print "Onbekend wapen!"
#
# TIP:
# Gebruik case _ voor een onbekende waarde.

# Stap 2 en Stap 4 code (inclusief de gevraagde comments en Bonus 1):
# We gebruiken een match case omdat dit overzichtelijker en netter is dan vele if-elif statements.
match selected_weapon:
    case "Sword":
        weapon_damage = 20
        print("Je gebruikt een zwaard!")
    case "Bow":
        weapon_damage = 15
        print("Je gebruikt een boog!")
    case "Staff":
        weapon_damage = 25
        print("Je gebruikt een magische staf!")
    case "Axe":
        weapon_damage = 30
        print("Je gebruikt een bijl!")
    # Bonus 1: Extra wapens toegevoegd
    case "Dagger":
        weapon_damage = 10
        print("Je gebruikt een snelle dolk!")
    case "Crossbow":
        weapon_damage = 22
        print("Je gebruikt een krachtige kruisboog!")
    case _:
        # Als het wapen niet bestaat, wordt de damage automatisch op 0 gezet.
        weapon_damage = 0
        print("Onbekend wapen!")


# Stap 3 - Resultaat printen
# Print na de match case de volgende informatie:
#
# Speler: Steve
# Wapen: Sword
# Damage: 20
#
# Zorg ervoor dat de informatie uit je variabelen komt.

# Stap 3 code:
print(f"Speler: {player_name}")
print(f"Wapen: {selected_weapon}")
print(f"Damage: {weapon_damage}")


# Stap 4 - Comments
# Voeg minimaal 3 eigen comments toe aan je programma.
# (Deze zijn hierboven bij Stap 1, 2 en de match case toegevoegd!)


# Stap 5 - Naming Conventions
# Controleer of je code voldoet aan de Python naming conventions.
# (Dit is gecontroleerd: we gebruiken snake_case, Engelse namen en kleine letters).


# BONUS 1
# Voeg zelf minimaal 2 nieuwe wapens toe aan je match case.
# (Toegevoegd in de match case bij Stap 2: "Dagger" en "Crossbow").


# BONUS 2
# Maak een variabele enemy_health met de waarde 100.
# Laat de speler 3 keer aanvallen met zijn gekozen wapen.
# Gebruik hiervoor een for-loop.
# Print na iedere aanval hoeveel health de vijand nog heeft.
# Zorg ervoor dat de health niet onder de 0 komt.

# Bonus 2 code:
enemy_health = 100
print("\n--- Bonus 2: 3 Aanvallen ---")
for i in range(3):
    enemy_health -= weapon_damage
    if enemy_health < 0:
        enemy_health = 0
    print(f"Vijand health over: {enemy_health}")


# BONUS 3
# Gebruik een while-loop om de vijand aan te vallen
# totdat de vijand geen health meer heeft.
# Print daarna "Vijand verslagen!"

# Bonus 3 code:
enemy_health = 100
print("\n--- Bonus 3: Gevecht tot het einde ---")
while enemy_health > 0:
    enemy_health -= weapon_damage
    if enemy_health < 0:
        enemy_health = 0
    print(f"Vijand health: {enemy_health}")

print("Vijand verslagen!")