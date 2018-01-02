from app import app
import os
import click


@app.cli.group()
def translate():
    """ Translation and locaization commands. """
    pass


@translate.command()
@click.argument('lang')
def init(lang='es'):
    """Initializing languages"""
    if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        raise RuntimeError("extract command failed")

    if os.system("pybabel init -i messages.pot -d app/translations -l " + lang):
        raise RuntimeError("init command failed")

    if os.system("python babel-google.py " + lang):
        raise RuntimeError("babel google failed")


@translate.command()
def update():
    """Update all languages."""
    if os.system("pybabel extract -F babel.cfg -k _l -o messages.pot ."):
        raise RuntimeError("extract command failed")

    if os.system("pybabel update -i messages.pot -d app/translations"):
        raise RuntimeError("update command failed")

    if os.system("python babel-google.py"):
        raise RuntimeError("babel google failed")

    os.remove("messages.pot")


@translate.command()
def compile():
    """Compile all languages."""
    if os.system("pybabel compile -d app/translations"):
        raise RuntimeError("compile command failed")
