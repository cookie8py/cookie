from application import app
from flask import render_template

@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html', login=False)

#다른 템플릿이 빌드될 때까지 'index'으로 연결됩니다.
@app.route("/courses")
def courses():
    return render_template('index.html')

@app.route("/register")
def register():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('index.html')


