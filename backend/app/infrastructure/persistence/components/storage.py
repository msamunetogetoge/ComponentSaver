import os
# from typing import Callable


def create_local_file_path(component_name: str) -> str:
    """
    コンポーネントを保存するパスを作成する。
    Args:
        component_name (str): コンポーネント名, hoge.vueなど

    Returns:
        str: app/infrastructure/persistence/components/hoge.vue など
    """

    base_path = "C:\\code\\python\\ComponentSaver\\backend\\app\\infrastructure\\persistence\\components\\files"
    return os.path.join(base_path, component_name)


# def create_s3_file_path(component_name: str) -> str:
#     # S3用のファイルパス生成ロジックを実装
#     pass


# # ストレージタイプに応じて適切な関数を指定
# file_path_generator: Callable[[str], str] = create_local_file_path
