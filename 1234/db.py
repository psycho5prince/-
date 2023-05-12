from sqlalchemy import create_engine, text
from sqlalchemy.orm import create_session, declarative_base
from sqlalchemy import Column, String

engine = create_engine("postgresql+psycopg2://postgres:univer@localhost/kR")
session = create_session(bind=engine)

class Auth():
    def isLogin(login, password):
        a = session.execute(text(f"SELECT * FROM auth WHERE login='{login}'")).fetchall()
        session.commit()
        session.close
        for i in a:
            if login == i[1]:
                if password == i[2]:
                    return True
                else:
                    continue
            else:
                return False