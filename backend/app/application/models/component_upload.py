from dataclasses import dataclass
from werkzeug.datastructures import FileStorage


@dataclass
class ComponentUpload:
    """flask のフォームからアップロードされるデータを扱うモデル
    """
    file_name: str
    file: FileStorage
    document: str
