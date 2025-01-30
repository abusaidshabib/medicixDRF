from datetime import timedelta
from django.conf import settings

ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:5173"
]
CSRF_TRUSTED_ORIGINS = [] + CORS_ALLOWED_ORIGINS

CORS_ALLOWED_ORIGIN_REGEXES = [] + CORS_ALLOWED_ORIGINS

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    # "ACCESS_TOKEN_LIFETIME": timedelta(seconds=10),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": settings.SECRET_KEY,
}