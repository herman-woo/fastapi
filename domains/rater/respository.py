from sqlmodel import Session, select
from .models import Rater
from db import engine

class RaterRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_table(self):
        """Ensure the Rater table is created."""
        Rater.metadata.create_all(engine)

    def save(self, Rater: Rater):
        """Insert a new Rater into the database."""
        self.session.add(Rater)
        self.session.commit()
        self.session.refresh(Rater)
        return Rater

    def find_by_id(self, Rater_id: int):
        """Retrieve a Rater by its ID."""
        return self.session.exec(select(Rater).where(Rater.id == Rater_id)).first()

    def find_all(self):
        """Retrieve all Raters."""
        return self.session.exec(select(Rater)).all()
    
    def delete(self, Rater_id: int):
        """Delete a Rater by ID."""
        Rater = self.find_by_id(Rater_id)
        if Rater:
            self.session.delete(Rater)
            self.session.commit()
            return True
        return False
