from app import app
from flask import render_template


@app.route('/add/<num1>/<num2>')
def display_sum(num1, num2):
    return render_template('index.html', var1=int(num1), var2=int(num2))
    # If not using html:
    # return str(int(num1) + int(num2))


@app.route('/')
def main_page():
    return render_template('main_page.html')
