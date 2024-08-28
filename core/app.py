import typer
import os   

from core import config, logic
from core.logic import ProjectType
from utils import colors

from core.commands import project


app = typer.Typer()

# Command Register
app.add_typer(project, name='project')


@app.command()
def info():
    print(f'App version: {config.read("app")["version"]}')


def run():
    app()
    