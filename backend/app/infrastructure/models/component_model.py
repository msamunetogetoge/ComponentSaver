
from dataclasses import dataclass


@dataclass
class ComponentModel:
    """DBと通信する為のコンポーネントモデル
    id :一意のid
    name: componentのファイル名(hogehoge.vyeなど)
    document: 表示したいドキュメント
    file_path: ファイルの保存場所
    created_by: User.id 後から追加するかも
    """
    id: int | None
    name: str
    document: str
    file_path: str
    created_by: int = 0
