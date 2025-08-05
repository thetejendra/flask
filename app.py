from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'secret123'  # Required for session/flash

# Simulated database (in-memory)
users = {}


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if not username or not password:
            flash('Username and password are required.')
            return redirect(url_for('register'))

        if username in users:
            flash('Username already exists.')
            return redirect(url_for('register'))

        users[username] = password
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password'].strip()

        if username in users and users[username] == password:
            session['username'] = username
            flash('Login successful.')
            return f"Welcome, {username}!"
        else:
            flash('Invalid credentials.')
            return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('Logged out.')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
