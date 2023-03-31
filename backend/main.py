import os
from typing import List

from flask import Flask, render_template, request, redirect, url_for

from werkzeug.utils import secure_filename

from app.application.models.component_upload_model import ComponentUpload
from app.application.models.view_model import ComponentView

from app.infrastructure.repositories.component_repository_db import ComponentRepositoryDB as Repository
from app.infrastructure.repositories.component_mapper import ComponentMapper
from app.infrastructure.repositories.component_view_mapper import ComponentViewMapper


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


@app.route("/")
def component_list():
    """/ にゲットリクエストが来た時の関数

    Returns:
        _type_: _description_
    """
    components = test_components
    components = repo.list()
    components = [ComponentViewMapper.to_view(
        ComponentMapper.to_model(component)) for component in components]
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
        component_from_flask = file.read().decode('utf-8')
        max_number = max([component.id for component in test_components])
        new_id = max_number + 1
        new_component_view = ComponentView(
            id=new_id, name=file_name, document=document)

        test_components.append(new_component_view)

        new_component: ComponentUpload = ComponentUpload(
            file_name=file_name, file=file, document=document)
        new_component.save_file()
        new_component.createComponentEntity

    # ファイルとその他のデータをデータベースに保存する処理を実装する（省略）

    # todo: ComponentUpload.save
    # コンポーネントのリストページにリダイレクト
    return redirect(url_for('component_list'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
