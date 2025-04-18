from sqlalchemy import Column, Integer, String
from src.models.modelsDb import Base

class Tipo(Base):
    __tablename__ = "Tipos"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID da tabela")
    nome = Column(String(200), nullable=True, comment="Tipo")
