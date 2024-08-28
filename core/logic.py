import os

from enum import Enum
from core import config


class ProjectType(Enum):
    PYTHON = 1

def create_project(name: str, type: ProjectType):
    if type == ProjectType.PYTHON:
        modules = config.read('python-project')['modules']    
        project_path = config.read('app')['projects-path']

        os.system(f'mkdir "{project_path}/{name}"')
        
        for module in modules:
            os.system(f'mkdir "{project_path}/{name}/{module}"')
            os.system(f'touch "{project_path}/{name}/{module}/__init__.py"')            
        
    