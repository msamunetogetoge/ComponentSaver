import os
from typing import List

from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS

from werkzeug.utils import secure_filename

from app.application.models.component_upload import ComponentUpload
from app.application.models.view_model import ComponentView
from app.application.services.component_service import ComponentService

from app.infrastructure.database import init_db
from app.infrastructure.repositories.component_repository_db import ComponentRepositoryDB as Repository


app = Flask(__name__, template_folder='app/infrastructure/api/templates')
CORS(app)

repo = Repository()
test_components: List[ComponentView] = [
    ComponentView(id=0, name="test_1",
                  document="test component_1"),
    ComponentView(id=1, name="test_2",
                  document="test component_2")
]
component_service = ComponentService(repo)


@app.route("/")
def component_list():
    """/ にゲットリクエストが来た時の関数

    Returns:
        _type_: _description_
    """
    components = component_service.get_all_comoponents()
    return render_template("component_form.html", components=components)


@app.route('/register_component', methods=['POST'])
def register_component():
    """コンポーネントを保存する関数

    Returns:
        Response : cpmponent_listのページを再度表示する
    """
    # フォームから送信されたデータを取得

    document = request.form.get('document', "")
    file = request.files.get('file')
    # test_components にデータを追加する
    if file and file.filename:
        file_name = secure_filename(file.filename)
        component_upload = ComponentUpload(
            file_name=file_name, file=file, document=document)
        # データをデータベースやファイルに保存する処理
        component_service.save_component(component_upload=component_upload)

    # コンポーネントのリストページにリダイレクト
    return redirect(url_for('component_list'))


@app.route("/components/<component_name>")
def get_component(component_name: str):
    """Componentを取得して、ComponentModelに詰めて渡す

    Args:
        component_id (int): ComponentModel.id = ComponentView.id

    Returns:
        _type_: _description_
    """
    # component_nameに対応するComponentを取得
    component = component_service.get_by_name(component_name)

    # エラーハンドリング（コンポーネントが見つからない場合）
    if component is None:
        return {"error": "Component not found"}, 404

    # Vueファイルの内容を含むComponentモデルをJSONとして返す
    return {
        "name": component.name,
        "document": component.document,
        "component_content": component.component_content
    }
    # return render_template("detail.html", component=component)


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
