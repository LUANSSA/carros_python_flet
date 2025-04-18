from sqlalchemy import Column, Integer, String
from src.models.modelsDb import Base

class Marcas(Base):
    __tablename__ = "Marcas"

    id = Column(primary_key=True, autoincrement=True, comment="ID da tabela")
    nome = Column(String(200), nullable=True, comment="Marca")