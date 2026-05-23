import random
import string

def generatePass(length=16):
    passwords = []
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    chiffre = random.choice(string.digits)
    symbole = random.choice(string.punctuation.replace(" ","").replace("\n",'').replace("|","").replace("[","").replace("]","").replace("(","").replace(")","").replace("`","").replace("'","").replace("{","").replace("}",""))

    allChars = string.ascii_letters + string.digits + string.punctuation.replace(" ","").replace("\n",'').replace("|","").replace("[","").replace("]","").replace("(","").replace(")","").replace("`","").replace("'","").replace("{","").replace("}","")
    reste = [random.choice(allChars) for _ in range(length - 4)]

    passwords = list(lowercase + uppercase + chiffre + symbole) + reste
    random.shuffle(passwords)
    password = ''.join(passwords)
    return password

saisie = input("Voulez-vous générer un mot de passe ? ")
password = generatePass()
if saisie.lower() in ("oui","yes"):
    print(password)