from app.application.models.component_upload import ComponentUpload

from app.application.mappers.component_mapper import map_component_upload_to_component
from app.application.mappers.component_view_mapper import ComponentViewMapper

from app.domain.repositories.component_repository import ComponentRepository

from app.infrastructure.persistence.components.storage import create_local_file_path
from app.infrastructure.repositories.component_mapper import ComponentMapper


class ComponentService:
    """
    Componentを保存するクラス
    """

    def __init__(self, component_repository: ComponentRepository):
        self.component_repository = component_repository

    def save_component(self, component_upload: ComponentUpload) -> None:
        """
            コンポーネントをローカルと、dbに登録する
        Args:
            component_upload (ComponentUpload): _description_
        """
        # ファイルを保存するディレクトリ

        # ファイルのフルパスを生成
        file_path = create_local_file_path(component_upload.file_name)

        # ファイルをディスクに保存
        component_upload.file.save(file_path)

        component = map_component_upload_to_component(
            component_upload=component_upload)
        # コンポーネントをdbに登録
        self.component_repository.add(component=component)

    def get_all_comoponents(self):
        components = self.component_repository.list()
        component_views = [
            ComponentViewMapper.to_view(ComponentMapper.to_model(component))
            for component in components
        ]
        return component_views
