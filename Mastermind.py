import random as rand

# Skriver ut information om spelet
print("Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.")
print("Du ska försöka gissa denna kods siffror på max 12 drag.")
print("Efter respektive gissning så kommer du att få en respons:")
print("För varje gissad korrekt siffra på korrekt plats i koden: ✓")
print("För varje gissad korrekt siffra på fel plats i koden: □")
print("För de siffror som inte finns med i koden ges ingen markering.")
print()

# Visar ett exempel på hur feedbacken fungerar
print("Exempel: om den slumpade koden är 2315")
print("och du gissar 3165")
print("så blir responsen ✓□□")
print()

# Informerar om de två svårighetsnivåerna
print("Du får välja mellan två svårighetsnivåer:")
print("Lättare nivå: Alla siffror är garanterat olika")
print("Svårare nivå: Det kan finnas upprepningar av en eller flera siffror")
print()

# Låter spelaren välja svårighetsnivå
while True:
    nivå = input("Ange önskad nivå: lättare (1), svårare (2) -> ")

    # Kontrollerar att spelaren har valt ett giltigt alternativ
    if nivå == "1" or nivå == "2":
        break

    print("Ange 1 eller 2.")

# Bestämmer om spelet ska fortsätta
spela = "ja"

# Gör det möjligt att spela flera gånger
while spela == "ja":

    # Skapar en tom lista för den hemliga koden
    kod = []

    # Fortsätter tills koden innehåller fyra siffror
    while len(kod) < 4:

        # Slumpar fram en siffra mellan 1 och 6
        siffra = rand.randint(1, 6)

        # Om spelaren valt lättare nivå
        if nivå == "1":

            # Kontrollerar att siffran inte redan finns i koden
            if siffra not in kod:

                # Lägger till siffran i koden
                kod.append(siffra)

        # Om spelaren valt svårare nivå
        else:

            # Lägger till siffran utan att kontrollera upprepningar
            kod.append(siffra)

    # Startar på 12 drag
    drag = 12

    # Skapar en lista för tidigare gissningar
    historik = []

    # Fortsätter så länge spelaren har drag kvar
    while drag > 0:

        print()

        # Ber spelaren att skriva sin gissning
        print("Ange gissning som följd av fyra siffror -> ", end="")

        # Kontrollerar att gissningen är korrekt
        while True:

            # Tar emot spelarens gissning
            gissning = input()

            # Kontrollerar att det är exakt fyra siffror
            if len(gissning) == 4 and gissning.isdigit():

                # Kontrollerar att siffrorna är mellan 1 och 6
                if all(1 <= int(s) <= 6 for s in gissning):
                    break

            # Ber spelaren försöka igen om gissningen är fel
            print("Ange fyra siffror mellan 1 och 6 -> ", end="")

        # Gör om gissningen till en lista med heltal
        gissning = [int(s) for s in gissning]

        # Räknar rätt siffror på rätt och fel plats
        rätt = 0
        fel = 0

        # Kopierar koden och gissningen
        kvar_kod = kod.copy()
        kvar_gissning = gissning.copy()

        # Kontrollerar siffror på rätt plats
        for i in range(4):

            # Om siffran på samma position är lika
            if gissning[i] == kod[i]:

                # Ökar antalet rätt placerade siffror
                rätt += 1

                # Tar bort siffrorna från kopiorna
                kvar_kod[i] = 0
                kvar_gissning[i] = 0

        # Kontrollerar siffror på fel plats
        for siffra in kvar_gissning:

            # Kontrollerar att siffran inte redan är borttagen
            # och att den finns i den hemliga koden
            if siffra != 0 and siffra in kvar_kod:

                # Ökar antalet siffror på fel plats
                fel += 1

                # Tar bort siffran så att den inte räknas igen
                kvar_kod.remove(siffra)

        # Skapar feedback med rätt antal symboler
        feedback = "✓" * rätt + "□" * fel

        # Sparar draget, gissningen och feedbacken
        historik.append((drag, gissning, feedback))

        # Skriver ut rubrikerna för historiken
        print()
        print("Drag #      Drag       Feedback")
        print("------------------------------------------")

        # Skriver ut alla tidigare gissningar
        for nummer, giss, respons in historik:

            # Gör om listan med siffror till en text
            gissning_text = ""

            # Lägger till varje siffra i texten
            for siffra in giss:
                gissning_text += str(siffra)

            # Skriver ut dragnummer, gissning och feedback
            print(nummer, "       ", gissning_text, "       ", respons)

        # Kontrollerar om spelaren har gissat hela koden rätt
        if rätt == 4:

            # Meddelar att spelaren har vunnit
            print()
            print("Snyggt :-)")
            break

        # Tar bort ett drag
        drag -= 1

    # Om spelaren inte lyckades gissa koden
    if rätt != 4:

        # Meddelar att alla drag är slut
        print()
        print("Du har slut på drag!")

        # Visar den hemliga koden
        kod_text = ""

        for siffra in kod:
            kod_text += str(siffra)

        print("Den rätta koden var:", kod_text)

    # Frågar om spelaren vill spela igen
    spela = input("\nVill du spela igen? (ja/nej) -> ").lower()

# Avslutar spelet
print("Tack för att du spelade!")