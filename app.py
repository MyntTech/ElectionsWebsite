from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name="home")

@app.route('/login')
def login():
    return render_template('login.html', name="login")

@app.route('/register')
def register():
    return render_template('register.html', name="register")


if __name__ == "__main__":
    app.run(debug=True)