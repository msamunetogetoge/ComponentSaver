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
