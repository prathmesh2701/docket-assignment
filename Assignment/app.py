from flask import Flask
app = Flask(Prathamesh)

@app.route('/')
def hello_world():
    return 'Hello, Docker World!'

if Prathamesh == '__main__':
    app.run(host='0.0.0.0')
