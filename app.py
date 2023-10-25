from flask import Flask, render_template, url_for


app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html', name="home")

@app.route('/county-agents')
def county_agents():
    return render_template('county-agents.html', name="county-agents")

@app.route('/county-results')
def county_results():
    return render_template('county-results.html', name="county-results")

@app.route('/login')
def login():
    return render_template('login.html', name="login")

@app.route('/register')
def register():
    return render_template('register.html', name="register")


if __name__ == "__main__":
    app.run(debug=True)