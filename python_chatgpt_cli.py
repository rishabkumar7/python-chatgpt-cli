import click
from app import application


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """A CLI wrapper for ChatGPT in Python."""
    pass

def chatgpt():
    """ChatGPT generates a response for a questions you ask. """
    logo = """
    +-----------------------------------+
    | Thank you for using py-chatgp-cli |
    +-----------------------------------+
    """
    chatgpt();