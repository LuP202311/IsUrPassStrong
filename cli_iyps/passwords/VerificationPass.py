import re
import typer
import os

app = typer.Typer()

    
def testMDP(mdp: str) -> tuple[bool, str, str, bool, str, bool]:
    """Étapes de test pour qu'un mot de passe soit valide"""

    isLong = False
    message = ""
    messageC = ""
    hasAllCharac = False
    messageO = ""
    isObvious = False

    # S'il contient tous les caractères demandés :

    if re.findall(r"^(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[^ \n])", mdp):
        hasAllCharac = True
        messageC = ""

        # Si le mot de passe apparaît dans le fichier des mots de passe facilement trouvés :

        dossier = os.path.dirname(__file__)
        chemin = os.path.join(dossier + "\\mdp_connues","mdp_connues.txt")

        mdpConnuesFile = open(chemin, "r", encoding="latin-1")
        fileContent = mdpConnuesFile.read().splitlines()
        mdpConnuesFile.close()

        for word in fileContent:
            if word.lower() in mdp.lower():
                isObvious = True
                messageO = "Le mot de passe figure dans la liste des mots de passe évidents."
                break
            else:
                isObvious = False
                messageO = ""
        
        # Vérification de la longueur :

        longueur = len(mdp)
        if longueur <= 8:
            isLong = False
            message = f"Le mot de passe est très faible ({longueur} caractères)."
        elif longueur <= 12:
            isLong = False
            message = f"Le mot de passe est faible ({longueur} caractères)."
        elif longueur <= 16:
            isLong = True
            message = ""
        else:
            isLong = True
            message = ""
    else:
        hasAllCharac = False
        messageC = "Le mot de passe doit contenir au moins un chiffre, une lettre en majuscule et minuscule."

    return isLong, message, messageC, hasAllCharac, messageO, isObvious

# Sans intéraction :
@app.command()
def mdp(mdp: str = typer.Argument(None, help="Vérifier la robustesse du mot de passe directement en ligne de commande")):  
    """Vérification de la robustesse d'un mot de passe"""

    isLong, message, messageC, hasAllCharac, messageO, isObvious = testMDP(mdp)

    while isLong and hasAllCharac and not isObvious:
        typer.echo(typer.style("Le mot de passe a tous les critères de robustesse.", fg=typer.colors.GREEN))
        raise typer.Exit()
    
    erreurs = "\n".join(filter(None, [message, messageC, messageO]))
    typer.echo(typer.style(erreurs, fg=typer.colors.RED))

# Avec intéraction :
@app.command()
def interactif():  
    mdp = typer.prompt("Veuillez saisir le mot de passe")

    isLong, message, messageC, hasAllCharac, messageO, isObvious = testMDP(mdp)

    while not isLong or not hasAllCharac or isObvious:
        erreurs = "\n".join(filter(None, [message, messageC, messageO]))
        typer.echo(typer.style(erreurs, fg=typer.colors.RED))
        re_mdp = typer.prompt("Veuillez re-saisir le mot de passe")
        isLong, message, messageC, hasAllCharac, messageO, isObvious = testMDP(re_mdp)
    typer.echo(typer.style("Le mot de passe a tous les critères de robustesse.", fg=typer.colors.GREEN))