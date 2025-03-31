# Créé par NGANJI, le 31/03/2025 en Python 3.7
'''Activité 1
Consigne
Écrire la fonction chiffrement(message: str, cle: int) → str qui code message.

On n’utilisera que des caractères majuscules ASCII dans le message et on supprimera les espaces.
Il faudra veiller à gérer le débordement de l’alphabet. Ainsi l’appel:
chiffrement("Z", 1)
'''

alph: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def chiffrement(message: str, cle: int) -> str:
    sortie = ""
    for lettre in message:
        # code ASCII de la lettre chiffrée
        code = ord(lettre) + cle
        # ajustement du code ASCII
        if code > ord("Z"):
            code = code-26
        # ajout
        sortie = sortie+chr(code)
    return sortie
chiffrement("BRAVO",15)
#'QGPKD'

'''version de Hristo de l'Activité 1'''

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def chiffrement(message, cle):
    res = ""
    recul = 0
    for i in range(len(message)):
        for j in range(26):
            if message[i] == alphabet[j]:
                if 26 - j > cle:
                    res += alphabet[j+cle]
                else:
                    res += alphabet[j+cle-26]
    return res
assert chiffrement("ABC",1) == "BCD"
assert chiffrement("Z", 1) == "A"

'''Activité 2
Consigne
Écrire la fonction dechiffrement(secret: str, cle: int) → str qui déchiffre secret en prenant en compte le débordement de l’alphabet
'''


'''version de Hristo de l'Activité 2'''
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def dechiffrement(secret, cle):
    res = ""
    for i in range(len(secret)):
        for j in range(26):
            if secret[i] == alphabet[j]:
                if 26 - j < cle:
                    res += alphabet[j-cle]
                else:
                    res += alphabet[j-cle]
    return res

assert dechiffrement("ABC",2) == "YZA"
assert dechiffrement("A", 1) == "Z"
