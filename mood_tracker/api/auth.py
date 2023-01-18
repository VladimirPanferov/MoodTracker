from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from ..models.auth import Token, User, UserCreate
from ..services.auth import AuthService, get_current_user

router = APIRouter(prefix="/auth")


@router.post("/sign-up", response_model=Token)
def sign_up(user_data: UserCreate, service: AuthService = Depends()):
    return service.register_new(user_data)


@router.post("/sign-in", response_model=Token)
def sign_in(
    form_data: OAuth2PasswordRequestForm = Depends(), service: AuthService = Depends()
):
    return service.authenticate(form_data.username, form_data.password)


@router.get("/list")
def list_users(auth_service: AuthService = Depends()):
    return auth_service.get_users()


@router.get("/user", response_model=User)
def get_user(user: User = Depends(get_current_user)) -> User:
    return user
