import typer
import os

from core.logic import ProjectType
from core import logic
from core import config
from utils import colors


app = typer.Typer()

@app.command()
def create():
    typer.echo('Project name:')
    name = input('> ')
    typer.echo('Language / Stack')
    project_type = input('> ')
    
    
    types = {
        "python": ProjectType.PYTHON,
        "py": ProjectType.PYTHON
    }
    
    for key, value in types.items():
        if project_type.lower() == 'list':
            
            msg = "List of supported languages\n"
            
            typer.echo(msg)
            break
            
        elif project_type.lower() == key:
            logic.create_project(name=name, type=value)
            os.system(f'code {config.read("app")["projects-path"]}')

@app.command()
def list():
    listed_directory = os.listdir(path=config.read('app')['projects-path'])
    output = "Listed Directorys:\n\n"
    
    for item in listed_directory:
        output += f"{item}\n"
    typer.echo(output)
    