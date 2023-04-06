
from sqlalchemy import Column, Integer, String
from app.infrastructure.database import Base


class ComponentModel(Base):
    """DBと通信する為のコンポーネントモデル
    id :一意のid
    name: componentのファイル名(hogehoge.vyeなど)
    document: 表示したいドキュメント
    file_path: ファイルの保存場所
    created_by: User.id 後から追加するかも
    """
    __tablename__ = "components"

    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True, unique=True)
    document: str = Column(String)
    file_path: str = Column(String)
    created_by: int = Column(Integer, default=0)
