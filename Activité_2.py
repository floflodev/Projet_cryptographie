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
    # Initialise une nouvelle phrase 
    nouvelle_phrase = ""
    for car in phrase :
        # Utilise la fonction chiffre_substitution_caractere 
        nouvelle_lettre_phrase = chiffre_substitution_caractere(car)
        # Défini la nouvelle phrase en ajoutant les caracteres au fur et a mesure 
        nouvelle_phrase += nouvelle_lettre_phrase
    return nouvelle_phrase
# Exemple avec la phrase "PAS DE POTION POUR OBELIX !"
resultat = chiffre_substitution_phrase("PAS DE POTION POUR OBELIX !")
print(resultat) # Affiche uyi od ubpgbn ubhq bkdxgs !

# 3)
# Objectif : 
# Programmer une fonction qui va déchiffrer une phrase codée par substitution

# On créer une premiere fonction servant a inverser notre mélange et l'alphabet
# A l'inverse de notre fonction chiffre_substitution_caractere qui passait de l'alphabet au mélange
# celle ci passe du mélange a l'alphabet 
def dechiffre_substitution_caractere(car) :
    if car not in Melange :
            return car
    i = Melange.index(car)
    j = Alphabet[i]
    return j 

# Cette fonction est construite de la meme maniere que la fonction chiffre_substitution_phrase
# Nous faisons cependant appel a la la fonction dechiffre_substitution_caractere 
def dechiffre_substitution_phrase(phrase) : 
    nouvelle_phrase = ""
    for car in phrase :
        nouvelle_lettre_phrase = dechiffre_substitution_caractere(car)
        nouvelle_phrase += nouvelle_lettre_phrase
    return nouvelle_phrase 
# Exemple avec la phrase "uyi od ubpgbn ubhq bkdxgs !"
resultat = dechiffre_substitution_phrase("uyi od ubpgbn ubhq bkdxgs !")
print(resultat) # Affiche PAS DE POTION POUR OBELIX !

