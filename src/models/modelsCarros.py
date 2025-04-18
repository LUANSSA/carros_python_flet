from sqlalchemy import Column, Integer, String, ForeignKey
from src.models.modelsDb import Base


class Carros(Base):
    __tablename__ = "Carros"
    # ID da tabela
    id = Column(Integer, primary_key=True, autoincrement=True, comment="ID da tabela")
    # Nome
    nome = Column(String(200), nullable=True, comment="Nome")
    # Descrição
    descricao = Column(String(4000), nullable=True, comment="Descrição")
    # Foto pequena
    fotoPequena = Column(String(20), nullable=True, comment="Foto pequena")
    # Foto média
    fotoMedia = Column(String(20), nullable=True, comment="Foto média")
    # Foto grande
    fotoGrande = Column(String(20), nullable=True, comment="Foto grande")
    # Ano
    ano = Column(String(11), nullable=True, comment="Data de lançamento")
    