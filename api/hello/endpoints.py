from api import app


@app.route('/')
def hello():
    return "I'm here!"
