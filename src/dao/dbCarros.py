from sqlalchemy import Column, Integer, String, ForeignKey
from dao.dao import Base


class Carros(Base):
    __tablename__ = "Carros"
    # ID da tabela
    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID da tabela")
    