from bottle import default_app, run
from bottle import request, response
from bottle import post
import re, json
import math 

#namepattern = re.compile(r'^[0-9]*$')

@post('/square')
def creation_handler():
    data = request.json
    result = int(data.get('number'))**2
    response.status = 200
    response.headers['Content-Type'] = 'application/json'
    response.body = json.dumps({ 'number': data.get('number'), 'result: ': result })
    return response

@post('/cube')
def creation_handler():
    data = request.json
    result = int(data.get('number'))**3
    response.status = 200
    response.headers['Content-Type'] = 'application/json'
    response.body = json.dumps({ 'number': data.get('number'), 'result: ': result })
    return response

@post('/squareroot')
def creation_handler():
    data = request.json
    result = math.sqrt(int(data.get('number')))
    response.status = 200
    response.headers['Content-Type'] = 'application/json'
    response.body = json.dumps({ 'number': data.get('number'), 'result: ': int(result) })
    return response

app = application = default_app()
if __name__ == '__main__':
    run(server='gunicorn', host = '127.0.0.1', port = 8000)
