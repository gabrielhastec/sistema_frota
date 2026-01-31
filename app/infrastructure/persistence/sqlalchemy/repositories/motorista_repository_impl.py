
from app.domain.repositories.motorista_repository import MotoristaRepository
from app.domain.entities.motorista import Motorista
from app.infrastructure.persistence.sqlalchemy.models import MotoristaModel
from app.infrastructure.persistence.sqlalchemy.session import SessionLocal

class MotoristaRepositoryImpl(MotoristaRepository):
    def __init__(self):
        self.session = SessionLocal()
    
    def salvar(self, motorista: Motorista):
        # Implementar conversão entity->model e persistência
        pass
