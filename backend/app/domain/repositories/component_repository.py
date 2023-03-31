from abc import ABC, abstractmethod
from typing import List, Optional

from app.domain.entities.component import Component


class ComponentRepository(ABC):

    @abstractmethod
    def add(self, component: Component) -> Component:
        pass

    @abstractmethod
    def get(self, component_id: int) -> Optional[Component]:
        pass

    @abstractmethod
    def list(self) -> List[Component]:
        pass

    @abstractmethod
    def update(self, component_id: int, component_data: Component) -> Optional[Component]:
        pass

    @abstractmethod
    def delete(self, component_id: int) -> bool:
        pass


class ComponentRepositoryInMemory(ComponentRepository):
    def __init__(self):
        self.components = []

    def add(self, component: Component) -> Component:
        self.components.append(component)
        return component

    def get(self, component_id: int) -> Optional[Component]:
        return next((component for component in self.components if component.id == component_id), None)

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
