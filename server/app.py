#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_param(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<int:integer_param>')
def count(integer_param):
    counter = ""
    for i in range(integer_param):
        counter += f'{i}\n'
    return counter

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == "*":
        return f'{num1 * num2 }'
    if operation == "+":
        return f'{num1 + num2 }'
    if operation == "-":
        return f'{num1 - num2 }'
    if operation == "div":
        return f'{num1 / num2 }'
    if operation == "%":
        return f'{num1 % num2 }'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
