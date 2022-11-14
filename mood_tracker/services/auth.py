from typing import List
from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import get_session
from ..models.auth import User
from .. import tables

class AuthService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_users(self) -> List[User]:
        return self.session.query(tables.User).all()