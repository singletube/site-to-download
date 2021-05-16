from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key_x'



@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/menu_page')
def menu_page():
    return render_template('menu_page.html')

@app.route('/download')
def download():
    return render_template('download_menu.html')




app.run(port=5555, host='127.0.0.1')