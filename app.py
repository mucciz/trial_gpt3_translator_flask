import os

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    

    return render_template('index.html', **locals())