from flask import Flask, send_from_directory


app = Flask(__name__, static_folder=None)


@app.route('/', defaults={'filename': 'index.html'})
@app.route('/<path:filename>')
def static_files(filename):
    print(filename)
    return send_from_directory('build/', filename)


@app.route('/api/hello')
def hello():
    return 'Hello, World!'
