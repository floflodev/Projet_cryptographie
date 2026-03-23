# Activité 2 
# Objectif général : Programmer un codage et décodage a partir d'un chiffrement de substitution 

# Les listes de références pour notre alphabet et notre mélange de substitution :
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Melange = "ykcodmfjgzaxrnbutqiphwesvl"

# 1) 
# Objectif :
# Programmer une fonction qui renvoie le caractere de l'alphabet chiffré par substitution 

def chiffre_substitution_caractere(car) :
    # Verifie si le caractere est dans notre alphabet
    if car not in Alphabet :
            # Si non, le retourne tel quel 
            return car
    # Trouve l'index du caractere dans l'alphabet
    i = Alphabet.index(car)
    # Recupere la nouvelle lettre correspondant a l'index 
    # au sein de notre mélange
    j = Melange[i]
    return j 
# Exemple avec A :
resultat = chiffre_substitution_caractere("A")
print(resultat) # Affiche y 

# 2)
# Objectif :
# Programmer une fonction qui renvoie une phrase codée par substitution 

def chiffre_substitution_phrase(phrase) :
    nouvelle_phrase = ""
    for car in phrase :
        nouvelle_lettre_phrase = chiffre_substitution_caractere(car)
        nouvelle_phrase += nouvelle_lettre_phrase
    return nouvelle_phrase
    
#resultat2 = chiffre_substitution_phrase("PAS DE POTION POUR OBELIX !")
#print(resultat2)
