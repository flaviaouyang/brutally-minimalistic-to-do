from flask import Flask, render_template, request
from sqlalchemy import null

app = Flask(__name__)

TO_DO_LIST = []

@app.route('/')
def index():
    print("/", TO_DO_LIST)
    return render_template('index.html', to_do_list = TO_DO_LIST)

@app.route('/todo', methods = ['POST'])
def todo():
    if request.form.get('todo') == '':
        print("add nothing: ",TO_DO_LIST)
        return render_template('index.html', to_do_list = TO_DO_LIST)
    if request.form.get('todo') != '':
        TO_DO_LIST.append(request.form.get('todo'))
        print("append: ",TO_DO_LIST)
        return render_template('index.html', to_do_list = TO_DO_LIST)

@app.route('/clear', methods= ['POST'])
def clear():
    TO_DO_LIST.clear()
    print("clear: ",TO_DO_LIST)
    return render_template('index.html', to_do_list = TO_DO_LIST)