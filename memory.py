from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine(
    "sqlite:///memory.db"
)


Base = declarative_base()


SessionLocal = sessionmaker(
    bind=engine
)



class Memory(Base):

    __tablename__="memory"


    id = Column(
        Integer,
        primary_key=True
    )


    command = Column(
        String
    )


    response = Column(
        String
    )



Base.metadata.create_all(
    engine
)