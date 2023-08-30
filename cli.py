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
DATABASE_URL = "sqlite:///comicdata.db"
engine = create_engine(DATABASE_URL)
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

@click.command()
@click.argument('username')
@click.argument('email')
def show_users():
    """Show all users"""
    session = Session()
    users = session.query(User).all()
    session.close()

    if users:
        user_choices = [
            (str(user.id), f"{user.username} - {user.email}") for user in users
        ]

        prompt_choices = [
            ('1', 'Show all users'),
            ('2', 'Show users by selection'),
            ('3', 'Exit')
        ]

        choice = click.prompt(
            "Select an option:",
            type=click.Choice([prompt_choice[0] for prompt_choice in prompt_choices])
        )

        if choice == '1':
            for user in users:
                click.echo(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
        elif choice == '2':
            selected_user_id = click.prompt(
                "Select a user:",
                type=click.Choice([choice[0] for choice in user_choices])
)
            selected_user = next((user for user in users if str(user.id) == selected_user_id), None)
            if selected_user:
                click.echo(f"Selected User: ID: {selected_user.id}, Username: {selected_user.username}, Email: {selected_user.email}")
            else:
                click.echo("User not found.")
        elif choice == '3':
            click.echo("Exiting...")
        else:
            click.echo("Invalid choice.")
    else:
        click.echo("No users found.")

cli.add_command(show_users)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    click.echo(BANNER)
    cli()
    show_users()
    
    
