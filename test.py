from flask import request

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1> your browser is %s </h1>  % User-Agent
