from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from settings import settings

security = HTTPBasic()


def basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    if not (
        settings.BASIC_AUTH_USER == credentials.username
        and settings.BASIC_AUTH_PASSWORD == credentials.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
