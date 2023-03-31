
from dataclasses import dataclass
from werkzeug.datastructures import FileStorage

from app.domain.entities.component import Component


@dataclass
class ComponentUpload:
    """flask のフォームからアップロードされるデータを扱うモデル
    """
    file_name: str
    file: FileStorage
    document: str
