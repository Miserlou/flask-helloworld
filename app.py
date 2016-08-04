from flask import Flask
app = Flask(__name__)

from flask import render_template

@app.route('/')
@app.route('/<name>')
def hello(name='World'):
    return render_template('hello.html', name=name)

def invoke_me():
    return "I have been invoked!"

def event_me(event, context):
    return "I am responding to an event!"
