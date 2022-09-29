import sqlalchemy
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import MetaData

# db: docker run -d --name postgresql-container --net dev-network -p 5432:5432 -e PGDATA=/pgdata -e POSTGRES_PASSWORD=p apilogicserver/postgres:version1.0.2

engine = create_engine("postgresql://postgres:p@localhost/postgres")
metadata = MetaData(engine)
metadata.reflect(engine)
print("open with metadata")