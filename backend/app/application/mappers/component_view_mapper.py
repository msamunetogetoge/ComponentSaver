from app.application.models.view_model import ComponentView
from app.infrastructure.models.component import ComponentModel
from app.infrastructure.persistence.components.storage import create_local_file_path


class ComponentViewMapper:
    """ComponentModel <-> ComponentViewの変換関数
    """
    @staticmethod
    def to_view(component_model: ComponentModel) -> ComponentView:
        """ComponentModel -> ComponentViewの変換関数

        Args:
            component_model (ComponentModel)

        Returns:
            ComponentView: 変換されたComponentView
        """
        component_id = component_model.id
        if component_id is None:
            component_id = 0
        return ComponentView(
            id=component_id,
            name=component_model.name,
            document=component_model.document
        )

    @staticmethod
    def to_model(component_view: ComponentView) -> ComponentModel:
        """ ComponentView -> ComponentModelの変換関数

        Args:
            component_view (ComponentView)

        Returns:
            ComponentModel: 変換されたComponentModel
        """
        return ComponentModel(
            id=component_view.id,
            name=component_view.name,
            document=component_view.document,
            # 適切な file_path を指定するか、別の方法で設定する
            file_path=create_local_file_path(component_view.name),
            created_by=0   # 適切な created_by を指定するか、別の方法で設定する
        )
