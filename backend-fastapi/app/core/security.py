
from datetime import UTC, datetime, timedelta
from typing import Any

import jwt
from pwdlib import PasswordHash

from app.core.config import settings

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
  return password_hash.hash(password)


def verify_password(plain_password:str, hashed_password:str) -> bool:
  return password_hash.verify(plain_password, hashed_password)


def create_access_token(subject: str, extra_claims: dict[str, Any] | None = None) -> str:
  expires_at = datetime.now(UTC) + timedelta(
    minutes=settings.access_token_expire_minutes
  )

  payload = dict[str, Any] = {
        "sub": subject,
        "type": "access",
        "exp": expires_at,
  }

  if extra_claims:
    payload.update(extra_claims)

  return jwt.encode(
    payload,
    settings.jwt_secret_key,
    algorithm=settings.jwt_algorithm
  )
