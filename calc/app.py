# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Calculate!</h1>
    <form method="POST">
        <input type="text" placeholder = 'Please type "add, sub, mult, or div" '
        <input type='text' placeholder='Please Type your first value' name="a" >
        <input type='text' placeholder='Please type your second value' name="b" >
        <button type='submit'>Submit</button>
    </form>
    """

@app.route('/add')
def add_operation():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a,b)

    return str(result)
@app.route('/sub')
def sub_operation():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = sub(a,b)

    return str(result)
@app.route('/div')
def div_operation():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = div(a,b)

    return str(result)
@app.route('/mult')
def mult_operation():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = mult(a,b)

    return str(result)
    
