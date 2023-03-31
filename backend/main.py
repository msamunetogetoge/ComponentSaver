import os
from typing import List

from flask import Flask, render_template, request, redirect, url_for

from werkzeug.utils import secure_filename

from app.application.models.component_upload import ComponentUpload
from app.application.models.view_model import ComponentView
from app.application.services.component_service import ComponentService

from app.infrastructure.database import init_db
from app.infrastructure.repositories.component_repository_db import ComponentRepositoryDB as Repository


app = Flask(__name__, template_folder='app/infrastructure/api/templates')

# UPLOAD_FOLDER = "app/infrastructure/persistence/components"
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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
    # components = test_components
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


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
