from dataclasses import dataclass


@dataclass
class Component:
    """
    vueやreactのコンポーネントとドキュメントを格納するモデル
    """
    id: int
    name: str
    document: str
    component: str = ""
