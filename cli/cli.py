import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

# Configure database connection

engine = create_engine("sqlite:///comicdata.db")
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    """Comic Selector"""

@cli.command()
@click.argument('username')
@click.argument('email')
def create_user(username, email):
    """Create a new user"""
    session = Session()
    user = User(username=username, email=email)
    session.add(user)
    session.commit()
    session.close()
    click.echo(f"User {username} created.")

if __name__ == '__main__':
    cli()