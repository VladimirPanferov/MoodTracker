from fastapi import APIRouter
from ..models.auth import User

router = APIRouter(prefix='/auth')

@router.get('/user', response_model=User)
def get_user():
    pass