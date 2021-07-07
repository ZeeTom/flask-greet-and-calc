from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    """Return "Welcome" greeting."""

    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>welcome</title>
</head>
<body>
    <h1>welcome</h1>
</body>
</html>
"""
    return html


@app.route('/welcome/home')
def say_welcome_home():
    """Return "Welcome" greeting."""

    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>welcome home</title>
</head>
<body>
    <h1>welcome home</h1>
</body>
</html>
"""
    return html

@app.route('/welcome/back')
def say_welcome_back():
    """Return "Welcome" greeting."""

    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>welcome back</title>
</head>
<body>
    <h1>welcome back</h1>
</body>
</html>
"""
    return html


