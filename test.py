from  flask import make_reponse

@app.route('/')
def index():
    response = make_response('<h1>this document carries a cookie</h1>')
    response.set_cookie('answer','35')
    return response


#just for a test
