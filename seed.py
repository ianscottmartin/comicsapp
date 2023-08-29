from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import User, Comic, Base, relationship


engine = create_engine("sqlite:///comicdata.db")
Session = sessionmaker(bind=engine)

def create_fake_users(session, total=10):
    fake = Faker()
    for _ in range(total):
        users = User(
            username=fake.user_name(),
            email=fake.email(),
        )
        
    session.add(users)
    session.commit()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()
    create_fake_users(session, total=20)
    session.commit()
    #session.bulk_save_objects(create_fake_users)
    
    
def create_fake_comics(session, total=10):
    fake = Faker()
    for _ in range(total):
        comics = Comic(
            title=fake.name(),
            issue_number=fake.random_int(min=1, max=100),
            publisher=fake.company(),
        )
    session.add(comics)
    session.commit()
    #session.bulk_save_objects(create_fake_comics)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()
    create_fake_users(session, total=20)
    create_fake_comics(session, total=15)  # Add fake comics
    session.commit()
    print("Database seeded with fake data.")
    


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()
    create_fake_users(session, total=20)
    create_fake_comics(session, total=15)
    
    
import ipdb; ipdb.set_trace()



