from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 実際のデータベースURLに変更してください
DATABASE_URL = ""

engine = create_engine(DATABASE_URL, isolation_level="AUTOCOMMIT")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def init_db():
    """db作成、テーブル作成
    """
    try:
        Base.metadata.create_all(bind=engine)
        print("db and table created!")
    except:
        print("create table failed")
