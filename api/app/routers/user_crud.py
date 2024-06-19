from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.models.classes.user_class import UserCreate
from app.services.postgre_connector import SessionLocal, engine
from app.security.hashing import get_password_hash
from app.models.classes.user_table import User
from app.models.classes.user_class import UserCreate, Token, TokenData
from app.security.token import get_current_user, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import datetime, timedelta
from app.models.user_operations import create_user, verify_user
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from fastapi.responses import HTMLResponse
import os

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Función para crear el token de acceso
async def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/create-account")
async def create_user_endpoint(user: UserCreate):
    user_id = create_user(user.username, user.password, user.role)
    if user_id:
        return {"username": user.username, "id": user_id, "role": user.role}
    else:
        raise HTTPException(status_code=400, detail="Error creating user")

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_info = verify_user(form_data.username, form_data.password)
    if not user_info:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username or password is incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

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







# Dependency
# async def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/register/")
# async def register_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = db.query(User).filter(User.email == user.email).first()
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     hashed_password = get_password_hash(user.password)
#     db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return {"username": db_user.username, "email": db_user.email}

# @router.get("/users/me/")
# async def read_user_me(current_user: User = Depends(get_current_user)):
#     return current_user

# @router.get("/dynamic/")
# async def dynamic_content(current_user: User = Depends(get_current_user)):
#     # Logic to return dynamic content
#     return {"message": f"Hello, {current_user.username}! This content is dynamic."}