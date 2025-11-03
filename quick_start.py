from flask import Flask, render_template, redirect, url_for, flash
import os

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-key-for-testing'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('tasks/dashboard.html', tasks=[], created_tasks=[])

@app.route('/chat')
def chat():
    return render_template('chat/chat.html')

@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.route('/register')
def register():
    return render_template('auth/register.html')

if __name__ == '__main__':
    app.run(debug=True)