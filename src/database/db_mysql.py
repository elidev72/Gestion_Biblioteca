import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

def url_db() -> str:
    USER_DB: str = os.getenv('DB_USER')
    PASS_DB: str = os.getenv('DB_PASSWORD')
    URL_DB: str = os.getenv('DB_HOST')
    NAME_DB: str = os.getenv('DB_NAME')
    return f'mysql+mysqlconnector://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

db = SQLAlchemy()

llave_secreta = os.getenv('SECRET_KEY')
