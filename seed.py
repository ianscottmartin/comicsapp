from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import User, Base


engine = create_engine("sqlite:///comicdata.db")
Session = sessionmaker(bind=engine)

def create_fake_users(session, total=10):
    fake = Faker()
    for _ in range(total):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
        )
        
    session.add(user)
    session.commit()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    session = Session()
    create_fake_users(session, total=20)
    session.close()
    print("Database seeded with fake data.")