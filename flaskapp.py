import form as form
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'button1':
            pass
        elif request.form.get('action2') == 'button2':
            pass
        else:
            pass
    elif request.method == 'GET':
        return render_template('index.html', form=form)

    return render_template('index.html')
