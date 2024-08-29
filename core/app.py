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
    print(f'\n{colors.WHITE}</project-creator>{colors.RESET}')
    print(f'App version: {colors.RED}{config.read("app")["version"]}{colors.RESET}\n')


def run():
    app()
    