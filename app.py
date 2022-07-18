from decouple import config
from flask import Flask, render_template, request, redirect, url_for
from translate_lang import get_translation

app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['aiPrompt']
        lang = request.form['language']
        answer = get_translation(text, lang)

    return render_template('index.html', **locals())