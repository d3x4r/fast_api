import databases
import sqlalchemy
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

USER = os.environ.get('USER')
URL = os.environ.get('URL')
PASSWORD = os.environ.get('PASSWORD')
DATABASE = os.environ.get('DATABASE')

DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{URL}/{DATABASE}"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
