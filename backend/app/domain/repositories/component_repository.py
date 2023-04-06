from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.component import Component


class ComponentRepository(ABC):

    @abstractmethod
    def add(self, component: Component) -> Component:
        """インサート処理をする

        Args:
            component (Component): _description_

        Returns:
            Component: 成功したコンポーネント
        """
        pass

    @abstractmethod
    def get(self, component_id: int) -> Optional[Component]:
        """idでコンポーネントを取得する

        Args:
            component_id (int): _description_

        Returns:
            Optional[Component]:
        """
        pass

    @abstractmethod
    def get_by_name(self, component_name: str) -> Optional[Component]:
        """nameでコンポーネントを取得する

        Args:
            component_name (str): _description_

        Returns:
            Optional[Component]:
        """
        pass

    @abstractmethod
    def list(self) -> List[Component]:
        """全てのコンポーネントを取得する

        Returns:
            List[Component]: 
        """
        pass

    @abstractmethod
    def update(self, component_id: int, component_data: Component) -> Optional[Component]:
        """コンポーネントを上書きする

        Args:
            component_id (int): _description_
            component_data (Component): _description_

        Returns:
            Optional[Component]: _description_
        """
        pass

    @abstractmethod
    def delete(self, component_id: int) -> bool:
        """コンポーネントを削除する

        Args:
            component_id (int): _description_

        Returns:
            bool: _description_
        """
        pass


class ComponentRepositoryInMemory(ComponentRepository):
    """メモリ内にコンポーネントモデルを作成する時のリポジトリ

    Args:
        ComponentRepository (_type_): _description_
    """

    def __init__(self):
        self.components = []

    def add(self, component: Component) -> Component:
        self.components.append(component)
        return component

    def get(self, component_id: int) -> Optional[Component]:
        return next((component for component in self.components if component.id == component_id), None)

    def get_by_name(self, component_name: str) -> Optional[Component]:
        return next((component for component in self.components if component.name == component_name), None)

    def list(self) -> List[Component]:
        return self.components

    def update(self, component_id: int, component_data: Component) -> Optional[Component]:
        component = self.get(component_id)
        if component:
            component.component_content = component_data.component_content
            component.document = component_data.document
            return component
        return None

    def delete(self, component_id: int) -> bool:
        component = self.get(component_id)
        if component:
            self.components.remove(component)
            return True
        return False
