from flask import Flask, render_template, request

app = Flask(__name__)

TO_DO_LIST = []

@app.route('/')
def index():
    return render_template('index.html', to_do_list = TO_DO_LIST)

@app.route('/todo', methods = ['POST'])
def todo():
    if not request.form.get('todo'):
        render_template('index.html', to_do_list = TO_DO_LIST)
    TO_DO_LIST.append(request.form.get('todo'))
    return render_template('index.html', to_do_list = TO_DO_LIST)

@app.route('/clear', methods= ['POST'])
def clear():
    TO_DO_LIST.clear()
    return render_template('index.html', to_do_list = TO_DO_LIST)