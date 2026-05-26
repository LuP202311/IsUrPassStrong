import typer

def help():
    typer.echo(typer.style("1. Pour vérifier si un mot de passe est robuste directement en commande: `python main.py verifier mdp ""<mot_de_passe>"""))
    typer.echo(typer.style("2. Pour vérifier si un mot de passe est robuste de manière interactive: `python main.py verifier interactif"))
    typer.echo(typer.style("3. Pour générer un mot de passe robuste: `python main.py generate"))