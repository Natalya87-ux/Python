from sqlalchemy import create_engine
from sqlalchemy.sql import select, insert, update, delete, text as txt
from sqlalchemy import MetaData

db_connection_string = "postgresql+psycopg2://postgres:Helotmst@localhost/QA"
engine = create_engine(db_connection_string)
metadata_obj = MetaData()
newid = 0
t = txt("SELECT MAX(USER_ID) FROM USERS")


def test_db_connection():
    t = txt("SELECT * FROM STUDENT")
    with engine.connect() as connection:
        result = connection.execute(t)
        assert result.rowcount == 1673


def test_db_insert():

    emailuser = "anal@mail.ru"
    subject = 1
    with engine.connect() as connection:
        ID = connection.execute(t).fetchone()[0]
        metadata_obj.reflect(bind=engine)
        ins = metadata_obj.tables["users"]
        newid = ID + 1
        intstr = insert(ins).values(
            user_id=newid, user_email=emailuser, subject_id=subject
        )
        connection.execute(intstr)
        connection.commit()
        assert connection.execute(t).fetchone()[0] == newid


def test_db_update():
    with engine.connect() as connection:
        metadata_obj.reflect(bind=engine)
        ins = metadata_obj.tables["users"]
        ID = connection.execute(t).fetchone()[0]
        de = update(ins).where(ins.c.user_id == ID).values(user_email="newemail@ay.ru")
        connection.execute(de)
        connection.commit()
        assert select(ins).where(ins.c.user_email == "newemail@ay.ru") != None


def test_db_delete():
    with engine.connect() as connection:
        metadata_obj.reflect(bind=engine)
        ins = metadata_obj.tables["users"]
        ID = connection.execute(t).fetchone()[0]
        de = delete(ins).where(ins.c.user_id == ID)
        connection.execute(de)
        connection.commit()
        assert connection.execute(t).fetchone()[0] == ID - 1

