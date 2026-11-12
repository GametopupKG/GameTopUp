import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


def resolve_database_url() -> str:
    default_db_path = (BASE_DIR / "database" / "app.db").resolve()
    raw_url = os.getenv("DATABASE_URL", f"sqlite:///{default_db_path.as_posix()}")

    if raw_url.startswith("sqlite:///"):
        relative_candidate = raw_url.replace("sqlite:///", "", 1)
        if relative_candidate and not os.path.isabs(relative_candidate):
            absolute_path = (BASE_DIR / relative_candidate).resolve()
            return f"sqlite:///{absolute_path.as_posix()}"
        return raw_url

    return raw_url or f"sqlite:///{default_db_path.as_posix()}"


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-change-me")
    SQLALCHEMY_DATABASE_URI = resolve_database_url()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    UPLOAD_FOLDER = BASE_DIR / "uploads"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@gametopup.kg")
