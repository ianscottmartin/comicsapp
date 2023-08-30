# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from faker import Faker
# from models import User, Comic, Base, relationship


# engine = create_engine("sqlite:///comicdata.db")
# Session = sessionmaker(bind=engine)

# def create_fake_users(session, total=10):
#     fake = Faker()
#     for _ in range(total):
#         users = User(
#             username=fake.user_name(),
#             email=fake.email(),
#         )
        
#     session.add(users)
#     session.commit()

# if __name__ == '__main__':
#     Base.metadata.create_all(engine)
#     session = Session()
#     create_fake_users(session, total=20)
#     session.commit()
#     session.bulk_save_objects(create_fake_users)
    
    
# def create_fake_comics(session, total=10):
#     fake = Faker()
#     for _ in range(total):
#         comics = Comic(
#             title=fake.name(),
#             issue_number=fake.random_int(min=1, max=100),
#             publisher=fake.company(),
#         )
#     session.add(comics)
#     session.commit()
#     #session.bulk_save_objects(create_fake_comics)


# if __name__ == '__main__':
#     Base.metadata.create_all(engine)
#     session = Session()
#     create_fake_users(session, total=20)
#     create_fake_comics(session, total=15)  # Add fake comics
#     session.commit()
#     print("Database seeded with fake data.")
#     # 


# # if __name__ == '__main__':
#     Base.metadata.create_all(engine)
#     session = Session()
#     create_fake_users(session, total=20)
#     create_fake_comics(session, total=15)
    
#     # 
    
# import ipdb; ipdb.set_trace()

from models import User, Comic



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///data.db")

Session = sessionmaker(bind=engine)
session = Session()


users = [
    User(username="Olaf"),
    User(username="Veronica"),
    User(username= "Brodie"),
    User(username="Silent Bob"),
    User(username= "Jay"),
    User(username="Holden"),
    User(username="Dante"),
    User(username="Randal"),
    User(username="Caitlin Bree"),
    User(username="Brad")
]

print(users)
session.bulk_save_objects(users)
session.commit()


session.query(User).delete()
session.commit()


comics = [
    Comic(title="Black Panther", publisher="Marvel"),
    Comic(title="Ironman", publisher="Marvel"),
    Comic(title="Xmen", publisher="Marvel"),
    Comic(title="XFactor", publisher="Marvel"),
    Comic(title="New Mutants", publisher="Marvel"),
    Comic(title="Spiderman", publisher="Marvel"),
    Comic(title="Avengers", publisher="Marvel"),
    Comic(title="Fantastic Four", publisher="Marvel"),
    Comic(title="Thor", publisher="Marvel"),
    Comic(title="Guardians of the Galaxy", publisher="Marvel"),
    Comic(title="ShadowHawk", publisher="Image"),
    Comic(title="Maxx", publisher="Image"),
    Comic(title="Wet Works", publisher="Image"),
    Comic(title="WildCats", publisher="Image"),
    Comic(title="Cyberforce", publisher="Image"),
    Comic(title="Walking Dead", publisher="Image"),
    Comic(title="Spawn", publisher="Image"),
    Comic(title="YoungBlood", publisher="Image"),
    Comic(title="Savage Dragon", publisher="Image"),
    Comic(title="Prophet", publisher="Image"),
    Comic(title="Justice League", publisher="DC"),
    Comic(title="Green Arrow", publisher="DC"),
    Comic(title="Nightwing", publisher="DC"),
    Comic(title="Flash", publisher="DC"),
    Comic(title="Teen Titans", publisher="DC"),
    Comic(title="Catwoman", publisher="DC"),
    Comic(title="Aquaman", publisher="DC"),
    Comic(title="Superman", publisher="DC"),
    Comic(title="Batman", publisher="DC"),
    Comic(title="Wonder Woman", publisher="DC"),
]

print(comics)
session.bulk_save_objects(comics)
session.commit()


session.query(Comic).delete()
session.query(User).delete()



