from datetime import UTC, datetime, timedelta

import jwt

from app.config import settings


def create_access_token(user_id: int) -> str:
    payload = {
        "sub": str(user_id),
        "exp": datetime.now(UTC)
        + timedelta(minutes=settings.access_token_expire_minutes),
    }

    return jwt.encode(payload, settings.secret_key, settings.algorithm)


def decode_access_token(token: str) -> int:
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            [settings.algorithm],
            options={"require": ["sub", "exp"]},
        )
        user_id = int(payload["sub"])

        if user_id <= 0:
            raise ValueError("Некорректный ID")
        return user_id
    except (jwt.exceptions.InvalidTokenError, ValueError) as exc:
        raise ValueError("Недействительный токен") from exc
