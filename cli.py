import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base

BANNER = """
      ______   ______   .___  ___.  __    ______      _______.
 /      | /  __  \  |   \/   | |  |  /      |    /       |
|  ,----'|  |  |  | |  \  /  | |  | |  ,----'   |   (----`
|  |     |  |  |  | |  |\/|  | |  | |  |         \   \    
|  `----.|  `--'  | |  |  |  | |  | |  `----..----)   |   
 \______| \______/  |__|  |__| |__|  \______||_______/    
                                                          
    
    
    """


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

import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Base

# ... (other imports and database setup)

@click.group()
def cli():
    """Comic Selector"""

# ... (other commands and functions)


@click.command()
def show_users():
    """Show all users"""
    session = Session()
    users = session.query(User).all()
    session.close()

    if users:
        user_choices = [(str(user.id), f"{user.username} - {user.email}") for user in users]
        selected_user_id = click.prompt("Select a user:", type=click.Choice([choice[0] for choice in user_choices]))
        selected_user = next((user for user in users if str(user.id) == selected_user_id), None)
        

    if selected_user:
            click.echo(f"Selected User: ID: {selected_user.id}, Username: {selected_user.username}, Email: {selected_user.email}")
    else:
            click.echo("User not found.")
   

cli.add_command(show_users)        



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    click.echo(BANNER)
    cli()




@click.group()
def cli():
    """"Comics"""
    



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    click.echo(BANNER)  # Print the banner
    cli()

    
