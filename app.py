import os
from flask import Flask,render_template,Blueprint
from flask_bootstrap import Bootstrap
from controller.start_controller import app_index


project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'view')
app = Flask(__name__, template_folder=template_path)
app.config['SECRET_KEY'] = "Dupa.123"

bootstrap = Bootstrap(app)

app.register_blueprint(app_index)

@app.route('/', methods=['GET', 'POST'])
def main_page():
    return render_template("start.html")


if __name__ == '__main__':
    app.run()