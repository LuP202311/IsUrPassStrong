import typer

from passwords import app as passwords_app
from version import app as version_app

app = typer.Typer(invoke_without_command=True)

app.add_typer(version_app)
app.add_typer(passwords_app, name="passwords")

@app.callback()
def default(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        typer.echo("Instructions :\n entrer dans le dossier ")

if __name__ == "__main__":
    app()