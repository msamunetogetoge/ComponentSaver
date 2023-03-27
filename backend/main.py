from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__, template_folder='app/infrastructure/api/templates')


@app.route("/")
def component_list():
    """/ にゲットリクエストが来た時の関数

    Returns:
        _type_: _description_
    """
    components = [
        {'name': 'Component1', 'description': 'This is a sample component.'},
        {'name': 'Component2', 'description': 'This is another sample component.'}
    ]
    return render_template("component_form.html", components=components)


@app.route('/register_component', methods=['POST'])
def register_component():
    """コンポーネントを保存する関数

    Returns:
        Response : cpmponent_listのページを再度表示する
    """
    # フォームから送信されたデータを取得
    name = request.form.get('name')
    description = request.form.get('description')
    file = request.files.get('file')

    # ファイルとその他のデータをデータベースに保存する処理を実装する（省略）

    # コンポーネントのリストページにリダイレクト
    return redirect(url_for('component_list'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000), debug=True)
