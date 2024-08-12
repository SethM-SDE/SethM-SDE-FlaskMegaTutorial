import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "uber-secret-key-you-cant-guess"
