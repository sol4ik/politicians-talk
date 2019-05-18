from sqlalchemy import Column, Integer, Unicode, UnicodeText, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////Desktop/politician-talk/data.db', echo=True)
Base = declarative_base(bind=engine)


class Convocation(Base):
    __tablename__ = 'convocations'

    id = Column(Integer, primary_key=True)

    no = Column(Integer, nullable=False)
    politicians_list = Column(nullable=False)
    sessions_calendar = Column(nullable=False)
    ideas = Column(nullable=False)
    ideas_rating = Column(nullable=False)

    def __init__(self, no, politicians_list, sessions_calendar, ideas, ideas_rating, amount=450):
        self.no = no

        self.politicians_amount = amount
        self.politicians_list = politicians_list
        self.sessions_calendar = sessions_calendar
        self.ideas = ideas
        self.ideas_rating = ideas_rating


Base.metadata.create_all()

Session = sessionmaker(bind=engine)
s = Session()


def to_db():
    """
    (py_object) -> None
    Adds given object to tha data.db.
    """
    pass
