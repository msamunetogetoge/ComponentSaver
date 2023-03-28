from flask import Flask, render_template, request, redirect, url_for
import os

from werkzeug.utils import secure_filename

from app.domain.repositories.component_repository import ComponentRepositoryInMemory as Reository
from app.domain.entities.component import Component


app = Flask(__name__, template_folder='app/infrastructure/api/templates')

repo = Reository()
test_components = [
    Component(id=0, component="", name="test_1",
              document="test component_1"),
    Component(id=1, component="", name="test_2",
              document="test component_2")
]
for component in test_components:
    repo.add(component=component)


@app.route("/")
def component_list():
    """/ にゲットリクエストが来た時の関数

    Returns:
        _type_: _description_
    """
    components = repo.list()
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
    if file and file.filename:
        file_name = secure_filename(file.filename)
        component_from_flask = file.read()
        max_number = max([component.id for component in repo.list()])
        new_component = Component(
            id=max_number+1, name=file_name, document=document, component=component_from_flask)
        repo.add(new_component)

    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
    # ファイルとその他のデータをデータベースに保存する処理を実装する（省略）

    # コンポーネントのリストページにリダイレクト
    return redirect(url_for('component_list'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
