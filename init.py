from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.orm import sessionmaker


# Указываем URL к базе данных
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/NTDC"

# Создаем объект движка
engine = create_engine(DATABASE_URL, echo=False)
metadata = MetaData()

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

parts = Table('parts', metadata, autoload_with=engine)
devices = Table('devices', metadata, autoload_with=engine)
journal = Table('journal', metadata, autoload_with=engine)
part_type = Table('part_type', metadata, autoload_with=engine)
operation = Table('operation', metadata, autoload_with=engine)
user = Table('user', metadata, autoload_with=engine)
status = Table('status', metadata, autoload_with=engine)
location =  Table('location', metadata, autoload_with=engine)