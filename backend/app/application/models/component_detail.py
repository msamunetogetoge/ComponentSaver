from dataclasses import dataclass


@dataclass
class ComponentDetailVue:
    """nuxtでvue コンポーネントを表示する時に使用するモデル
    """
    file_name: str
    document: str
    template: str
    script: str
    style: str
