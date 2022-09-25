#!/usr/bin/env python

import click


@click.group()
def cli():
    """click group cli subcommand test"""

@cli.command()
@click.option('--string', default = "world", help = "Enter your name after --string command")
@click.option('--repeat', default = 1, help = "Enter the times you want to repeat")
def say(string, repeat):
    """Hello World!"""
    for x in range (1,repeat):
        click.echo("hello %s..." % string)


if __name__ == "__main__":
    cli()