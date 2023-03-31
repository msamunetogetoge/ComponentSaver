from app.domain.entities.component import Component
from app.infrastructure.models.component_model import ComponentModel
from app.infrastructure.persistence.components.storage import create_local_file_path


class ComponentMapper:
    """Component <->ComponentModelのマッパー

    Returns:
        _type_: _description_
    """
    @staticmethod
    def to_entity(component_model: ComponentModel) -> Component:
        """ComponetnModel -> Component

        Args:
            component_model (ComponentModel)

        Returns:
            Component
        """
        component_content = open(
            component_model.file_path, encoding="utf-8").read()
        return Component(
            name=component_model.name,
            document=component_model.document,
            component_content=component_content
        )

    @staticmethod
    def to_model(component: Component, created_by: int = 0) -> ComponentModel:
        """Component -> ComponentModel

        Args:
            component (Component): _description_
            created_by (int, optional): _description_. Defaults to 0.

        Returns:
            ComponentModel: 注意: file_pathはローカルに作成している
        """
        return ComponentModel(
            id=None,
            name=component.name,
            document=component.document,
            file_path=create_local_file_path(component.name),
            created_by=created_by
        )
