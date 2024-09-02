
import os

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.get_env("DB_NAME", "test")
DB_CONNECTION_STRING = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

DOCS_BUCKET = os.getenv("DOCS_BUCKET", "docs")
APP_RUNNER_BASE_URL = os.getenv("APP_RUNNER_BASE_URL", "http://localhost:8000")