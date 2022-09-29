import sqlalchemy
from sqlalchemy.engine import create_engine
from sqlalchemy.schema import MetaData
import sqlalchemy.dialects.postgresql.base as pg_dialect
from sqlalchemy import CHAR, Column, DateTime, Float, ForeignKey, Index, Integer, String, TIMESTAMP, Table, Text, UniqueConstraint, text

# db: docker run -d --name postgresql-container --net dev-network -p 5432:5432 -e PGDATA=/pgdata -e POSTGRES_PASSWORD=p apilogicserver/postgres:version1.0.2

substitute_char = True
if substitute_char:
    pg_dialect.ischema_names["bpchar"] =  CHAR

engine = create_engine("postgresql://postgres:p@localhost/postgres")
# engine = create_engine("postgres+psycopg2://postgres:p@localhost/postgres")  # fails with 'no such module'

metadata = MetaData(engine)
metadata.reflect(engine)

print("open with metadata")