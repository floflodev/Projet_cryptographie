# Activité 3 
# Objectif général : Utiliser la fréquence d'apparition des lettres pour déchiffrer un message en essayant de deviner la substitution 

# La liste servant de référence pour notre alphabet :
Alphabet = "abcdefghijklmnopqrstuvwxyz"

# 1)
# Objectif :
# Programmer une fonction qui réalise une substitution de lettres basée sur deux alphabets
# Elle remplace nos lettres de départ par les lettres connues de notre alphabet d'arrivée

# On initialise un alphabet de départ, basé sur notre alphabet
Alphabet_depart = "abcdefghijklmnopqrstuvwxyz"
# On initialise un alphabet d'arrivé (donné dans l'énoncé)
Alphabet_arrivee = "...S.....E..T............."

def substitution(phrase, Alphabet_depart, Alphabet_arrivee) :
    # On initialise une nouvelle chaine vide pour notre nouvelle phrase
    nouvelle_phrase = ""
    for car in phrase : 
        # On verifie que notre caractere est dans notre alphabet de départ
        if car not in Alphabet_depart :
            # Si non, on l'ajoute tel quel
            nouvelle_phrase += car 
        else :
            # Si oui, on trouve l'index du caractere dans cet alphabet 
            i = Alphabet_depart.index(car)
            # On ajoute a la nouvelle phrase le caractere correspondant a l'index dans l'alphabet d'arrivee 
            nouvelle_phrase += Alphabet_arrivee[i]  
    return nouvelle_phrase
# Exemple avec la phrase "jdolwt jd tm vb ?" et nos deux alphabets selectionnés
resultat = substitution("jdolwt jd tm vb ?", Alphabet_depart, Alphabet_arrivee)
print(resultat) #Affiche "ES.... ES .T .. ?"
# Erreur de l'énoncé :
# Dans l'énoncé il est écrit qu'en utilisant la phrase "jdolwt jd tm vb ?" nous obtiendrons "ES...T ES T. .. ?"
# Afin de deviner "Esprit es tu la ?" mais le resultat est bien : ES.... ES .T .. ?

# 2) 
# Objectif :
# Programmer une fonction 
