from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__, template_folder='templates', static_folder='static')

users = {
    "user1": "password1",
    "user2": "password2",
}

def generate_dummy_users():
    for i in range(1, 101):
        username = f"user{i}"
        password = f"password{i}"
        users[username] = password

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return redirect(url_for('welcome', username=username))
    else:
        return "Invalid credentials. Please try again."

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        new_username = request.form['new_username']
        new_password = request.form['new_password']

        if new_username not in users:
            users[new_username] = new_password
            return redirect(url_for('welcome', username=new_username))
        else:
            return "Username already exists. Please choose a different username."
    return render_template('signup.html')

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html', username=username)

if __name__ == '__main__':
    generate_dummy_users()
    app.run(debug=True)
    app = Flask(__name__, static_url_path='/static')