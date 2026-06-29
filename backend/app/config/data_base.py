from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/avisos_ciudadanos_db"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def init_db():
    from app.entity.usuario import UsuarioORM
    from app.entity.aviso import AvisoORM
    from app.entity.seguimiento import SeguimientoORM

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        admin = db.query(UsuarioORM).filter_by(correo="admin@gmail.com").first()

        if not admin:
            admin = UsuarioORM(
                "000000000",
                "Administrador del Sistema",
                "admin@gmail.com",
                "admin123",
                "administrador"
            )

            db.add(admin)
            db.commit()

    finally:
        db.close()