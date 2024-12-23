from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, mundo! Esta es mi página Flask en Heroku."

if __name__ == '__main__':
    app.run()
