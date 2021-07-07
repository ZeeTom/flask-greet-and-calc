from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1>Testing</h1>
  </body>
</html>
    """


@app.route('/add')
def add():
    """Add a and b."""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a + b)





@app.route('/sub')
def sub():
    """Subtract b from a."""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a - b)






@app.route('/mult')
def mult():
    """Multiply a and b."""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a * b)





@app.route('/div')
def div():
    """Divide a by b."""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    return str(a / b)
