import re

def isMDPLong(MDP):
    isLong = True
    message = ""
    if len(MDP) < 8:
        isLong = False
        message = "Le mot de passe est très faible, il a seulement " + str(len(MDP)) + " caractères."
    elif 8 <= len(MDP) <= 12:
        isLong = False
        message = "Le mot de passe est faible, il a seulement " + str(len(MDP)) + " caractères."
    elif 12 < len(MDP) <= 16:
        isLong = True
        message = ""
    else:
        isLong = True
        message = ""
    return isLong, message

def usedAllCharac(MDP):
    if re.findall(r"^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[^ \n])", MDP):
        hasAllCharac = True
        messageC = ""
    else:
        hasAllCharac = False
        messageC = "Le mot de passe doit contenir au moins un chiffre, une lettre en majuscule et minuscule"
    return messageC, hasAllCharac

def isMDPobvious(MDP):
    #rockYouFile = open("./rockyou/rockyou.txt", "r", encoding="latin-1")
    #fileContent = rockYouFile.read()
    mdpConnuesFile = open("./mdp_connues/mdp_connues.txt", "r", encoding="latin-1")
    fileContent = mdpConnuesFile.read().splitlines()
    for word in fileContent:
        if word in MDP:
            isObvious = True
            messageO = "Le mot de passe est trop évident"
            break
        else:
            isObvious = False
            messageO = ""
    mdpConnuesFile.close()
    return messageO, isObvious
    
saisie = input("Veuillez saisir le mot de passe: ")
isLong, message = isMDPLong(saisie)
messageC, hasAllCharac = usedAllCharac(saisie)
messageO, isObvious = isMDPobvious(saisie)

while not isLong or not hasAllCharac or not isObvious:
    print(message + "\n" + messageC + "\n" + messageO)
    resaisie = input("Veuillez re-saisir le mot de passe: ")
    isLong, message = isMDPLong(resaisie)
    messageC, hasAllCharac = usedAllCharac(resaisie)
    messageO, isObvious = isMDPobvious(resaisie)

print(message + "\n" + messageC + "\n" + messageO)