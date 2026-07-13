# sqlalchemy_app/models.py
import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# a & b. Tabela pośrednicząca do obsługi relacji wiele-do-wielu (Zadanie 9)
zadanie_tag = Table(
    'zadanie_tag',
    Base.metadata,
    Column('zadanie_id', Integer, ForeignKey('zadania.id', ondelete="CASCADE"), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tagi.id', ondelete="CASCADE"), primary_key=True)
)

# a. Nowy model Tag (Zadanie 9)
class Tag(Base):
    __tablename__ = 'tagi'
    
    id = Column(Integer, primary_key=True)
    nazwa = Column(String, unique=True, nullable=False)
    
    # c. Zdefiniowanie relacji w modelu Tag
    zadania = relationship("Zadanie", secondary=zadanie_tag, back_populates="tagi")

    def __repr__(self):
        return f"<Tag (id={self.id}, nazwa='{self.nazwa}')>"


class Zadanie(Base):
    __tablename__ = 'zadania'
    
    id = Column(Integer, primary_key=True)
    opis = Column(String, nullable=False)
    zrobione = Column(Boolean, default=False, nullable=False)
    data_utworzenia = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    
    # c. Zdefiniowanie relacji w modelu Zadanie
    tagi = relationship("Tag", secondary=zadanie_tag, back_populates="zadania")

    def __repr__(self):
        return f"<Zadanie (id={self.id}, opis='{self.opis}', zrobione={self.zrobione})>"