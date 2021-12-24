from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

def getOpenConnection(session):
    Session = session
    def OpenConnection(func):
        def wrap(*args, **kwargs):
            with Session() as session, session.begin():
                f = func(*args, **kwargs, session=session)
            return f
        return wrap
    return OpenConnection

# ============== Start the database and migrations ==============
class DataBaseSQL():
    def __init__(self, pg_url_db: str, base_models: declarative_base) -> None:
        self.pg_url_db = pg_url_db
        self.base_models = base_models
        self.engine = None
        self.Session = None

    def __init_database(self) -> None:
        self.engine = create_engine(self.pg_url_db, pool_size=50, max_overflow=0, pool_recycle=3600)
        self.Session = sessionmaker(bind=self.engine)

    def __start_migrations(self) -> None:
        self.base_models.metadata.create_all( self.engine )

    def start(self) -> Session:
        self.__init_database()
        self.__start_migrations()
        return getOpenConnection(self.Session)
    

# ======= Open a connection to the database, using a decorator =======
# from types import MethodType
# class OpenConection(object):
#     def __init__(self, func) -> None:
#         self.func = func

#     def __call__(self, *args, **kwargs) -> None:
#         with self.Session() as session, session.begin():
#             return self.func(*args, **kwargs, session=session)

#     def __get__(self, instance, cls) -> None:
#         return self if instance is None else MethodType(self, instance)