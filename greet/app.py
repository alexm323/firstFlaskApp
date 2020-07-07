from flask import Flask

app = Flask(__name__)

@app.route('/')
def greet():
    return 'The home page'

@app.route('/<welcome>')
def welcome(welcome):
    return 'welcome'

@app.route('/<welcome>/home')
def home(welcome):
    return 'welcome home'
@app.route('/<welcome>/back')
def back(welcome):
    return 'welcome back'