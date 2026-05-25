import typer

from .VerificationPass import app as verification_app
from .GeneratePass import app as generate_app

app = typer.Typer()

app.add_typer(verification_app, name="verifier")
app.add_typer(generate_app)