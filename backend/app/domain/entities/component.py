from dataclasses import dataclass


@dataclass
class Component:
    """
    vueやreactのコンポーネントとドキュメントを格納するモデル
    """
    name: str
    document: str
    component_content: str = ""