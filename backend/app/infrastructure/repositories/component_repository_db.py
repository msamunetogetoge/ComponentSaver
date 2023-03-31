from typing import List, Optional

from app.domain.entities.component import Component
from app.domain.repositories.component_repository import ComponentRepository

from app.infrastructure.repositories.component_mapper import ComponentMapper
from app.infrastructure.database import SessionLocal
from app.infrastructure.models.component import ComponentModel
from app.infrastructure.persistence.components.storage import create_local_file_path


class ComponentRepositoryDB(ComponentRepository):
    """DBと接続して、Componentのデータをやり取りするリポジトリ。
    DB接続の実装はapp.infrastructure.database にある
    """

    def add(self, component: Component) -> Component:
        """insert component

        Args:
            component (Component): insertするcomponent

        Returns:
            Component: 
        """
        session = SessionLocal()
        component_model = ComponentMapper.to_model(component=component)
        try:
            session.add(component_model)
            session.commit()
            session.refresh(component_model)
            return ComponentMapper.to_entity(component_model=component_model)
        finally:
            session.close()

    def get(self, component_id: int) -> Optional[Component]:
        session = SessionLocal()
        try:
            component = session.query(ComponentModel).filter(
                ComponentModel.id == component_id).one_or_none()
            return component
        finally:
            session.close()

    def list(self) -> List[Component]:
        session = SessionLocal()
        try:
            component_list = session.query(ComponentModel).all()
            return component_list
        finally:
            session.close()

    def update(self, component_id: int, component_data: Component) -> Optional[Component]:
        session = SessionLocal()
        try:
            component: ComponentModel | None = session.query(ComponentModel).filter(
                ComponentModel.id == component_id).one_or_none()
            if component is not None:
                component.id = component_id
                component.name = component_data.name
                component.file_path = create_local_file_path(
                    component_data.name)
                session.add(component)
                session.commit()
                session.refresh(component)
                return ComponentMapper.to_entity(component_model=component)
            else:
                return None
        finally:
            session.close()

    def delete(self, component_id: int) -> bool:
        session = SessionLocal()
        try:
            component: ComponentModel | None = session.query(ComponentModel).filter(
                ComponentModel.id == component_id).one_or_none()
            if component is not None:

                session.delete(component)
                session.commit()
                return True
            else:
                return True
        except:
            return False
        finally:
            session.close()

# @dataclass
# class User:
#     """ユーザークラス.後から使うかも
#     """
#     id: int
#     password: str
#     name: str
