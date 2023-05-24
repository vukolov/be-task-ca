from .database import engine, Base

# just importing all the models is enough to have them created
# flake8: noqa
from .user import model1
from .item import model2


def create_db_schema():
    Base.metadata.create_all(bind=engine)
