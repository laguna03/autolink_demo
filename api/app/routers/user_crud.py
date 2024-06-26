from fastapi import APIRouter, HTTPException, Depends, status
from app.models.classes.user_class import UserCreate, Token, TokenData
from app.security.token import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import datetime, timedelta
from app.models.user_operations import create_user, verify_user, create_access_token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError,jwt
from fastapi.responses import HTMLResponse
import logging
import os

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/create_account")
async def create_user_endpoint(user: UserCreate) -> dict:
    logging.info(f"Received data: {user}")
    try:
        user_id = create_user(user.username, user.email, user.password)
        if user_id is None:
            raise HTTPException(status_code=500, detail="Error creating user")
        return {"message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> dict:
    try:
        user_info = verify_user(form_data.username, form_data.password)
        if not user_info:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Username or password is incorrect",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user_info["username"]}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException as e:
        raise e
    except Exception as e:
        print("Unexpected error:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/users/me/", response_model=TokenData)
async def read_users_me(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credentials are invalid",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    return token_data

# Usar la ruta absoluta a tus archivos HTML
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "static/html")

@router.get("/", response_class=HTMLResponse)
async def read_root():
    with open(os.path.join(TEMPLATE_DIR, "create_agent.html"), "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@router.get("/login", response_class=HTMLResponse)
async def get_login():
    with open(os.path.join(TEMPLATE_DIR, "login.html"), "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@router.get("/create-account", response_class=HTMLResponse)
async def get_create_account():
    with open(os.path.join(TEMPLATE_DIR, "create_account.html"), "r") as f:
        return HTMLResponse(content=f.read(), status_code=200)
