from dataclasses import dataclass


@dataclass
class ComponentView:
    """backend/app/infrastructure/api/templates/component_form.html でデータを表示する時のモデル
    """
    id: int
    name: str
    document: str
