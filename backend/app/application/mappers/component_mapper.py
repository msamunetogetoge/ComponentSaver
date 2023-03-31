from app.infrastructure.persistence.components.storage import create_local_file_path
from app.infrastructure.models.component import ComponentModel
from app.domain.entities.component import Component
from app.application.models.component_upload import ComponentUpload


def map_component_upload_to_component(component_upload: ComponentUpload) -> Component:
    """ComponentUploadからComponentへのマッピングロジックを実装

    Args:
        component_upload (ComponentUpload)

    Returns:
        Component: マッピングされたComponent
    """
    #
    component_content = component_upload.file.read().decode("utf-8")
    return Component(
        name=component_upload.file_name,
        document=component_upload.document,
        component_content=component_content
    )


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
