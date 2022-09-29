import sqlalchemy
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import MetaData

engine = create_engine("postgresql://postgres:p@localhost/postgres")
metadata = MetaData(engine)
metadata.reflect(engine)
print("open with metadata")