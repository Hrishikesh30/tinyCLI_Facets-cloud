import click
import os

@click.group()
def cli():
    pass

@cli.command()
@click.option("--name",prompt="Enter your name",help="The name of the user")
def hello(name):
    click.echo(f"hello {name}!")

@cli.command()
@click.argument("file")
def record(file):
    curr_path = os.path.abspath(file)
    print(f"Reading file at: {curr_path}")

    try:
        with open(curr_path, "r") as f:
            contents = f.read()
            print("File Contents:\n", contents)
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Unable to read file.")

if __name__ == "__main__":
    cli()