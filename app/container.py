
from dependency_injector import containers, providers
from app.infrastructure.persistence.sqlalchemy.database import SessionLocal
from app.infrastructure.persistence.sqlalchemy.repositories.motorista_repository_impl import MotoristaRepositoryImpl

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.routes.motoristas",
            "app.api.v1.routes.veiculos",
        ]
    )
    
    session = providers.Factory(SessionLocal)
    
    # Repositórios
    motorista_repository = providers.Factory(
        MotoristaRepositoryImpl,
        session=session
    )
