import secrets
import string
import typer
import re
import random

app = typer.Typer()

def createPass(length=16):
    symboles_enlevés = re.sub(r'[ \n|\[\](){}`\'<>,".:+-~\*\\]', '', string.punctuation)

    passwords = []
    lowercase = secrets.choice(string.ascii_lowercase)
    uppercase = secrets.choice(string.ascii_uppercase)
    chiffre = secrets.choice(string.digits)
    symbole = secrets.choice(symboles_enlevés)

    allChars = string.ascii_letters + string.digits + symboles_enlevés
    reste = [secrets.choice(allChars) for _ in range(length - 4)]

    passwords = list(lowercase + uppercase + chiffre + symbole) + reste
    random.shuffle(passwords)
    password = ''.join(passwords)
    return password

@app.command()
def generatePass(generate:bool = typer.Option(False,"--generate","-g",help="Générer un mot de passe")):
    """Générer un mot de passe robuste"""

    if generate:
        password = createPass()
        typer.echo(typer.style(f"Voici le mot de passe généré: {password}",fg=typer.colors.GREEN))
    else:
        typer.echo(typer.style("Saisissez `python GeneratePass.py --generate` ou `python GeneratePass.py -g` pour générer un mot de passe",fg=typer.colors.CYAN))

if __name__ == '__main__':
    app()