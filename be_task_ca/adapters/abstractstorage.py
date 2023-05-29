from sqlalchemy.orm import Session


class AbstractStorage:
    def __init__(self, db: Session):
        self.db = db
