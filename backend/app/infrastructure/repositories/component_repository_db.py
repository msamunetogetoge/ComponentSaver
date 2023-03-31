from typing import List, Optional


from app.domain.repositories.component_repository import ComponentRepository
from app.domain.entities.component import Component


class ComponentRepositoryDB(ComponentRepository):

    def add(self, component: Component) -> Component:
        pass

    def get(self, component_id: int) -> Optional[Component]:
        pass

    def list(self) -> List[Component]:
        pass

    def update(self, component_id: int, component_data: Component) -> Optional[Component]:
        pass

    def delete(self, component_id: int) -> bool:
        pass

# @dataclass
# class User:
#     """ユーザークラス.後から使うかも
#     """
#     id: int
#     password: str
#     name: str
