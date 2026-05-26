import typer

from passwords import app as passwords_app
from version import app as version_app
from help import app as help_app

app = typer.Typer(invoke_without_command=True)

app.add_typer(version_app)
app.add_typer(passwords_app, name="passwords")
app.add_typer(help_app)

@app.callback()
def default(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        typer.echo("Voici les instructions pour tester le programme avec la CLI: \n1. Entrez dans le dossier `cli_iyps` (avec la commande `cd cli_iyps`)\n2. Pour découvrir toutes les commandes, tapez `python main.py help`")

if __name__ == "__main__":
    app()
