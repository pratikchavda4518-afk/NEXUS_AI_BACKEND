from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)



DATABASE_URL = "sqlite:///ai_settings.db"



engine = create_engine(

    DATABASE_URL,

    connect_args={
        "check_same_thread": False
    }

)



Base = declarative_base()



SessionLocal = sessionmaker(

    autocommit=False,

    autoflush=False,

    bind=engine

)




class AISettings(Base):

    __tablename__ = "settings"



    id = Column(

        Integer,

        primary_key=True

    )



    name = Column(

        String,

        default="NEXUS"

    )



    mode = Column(

        String,

        default="ACTIVE"

    )



    voice = Column(

        String,

        default="ENGLISH"

    )




Base.metadata.create_all(

    bind=engine

)