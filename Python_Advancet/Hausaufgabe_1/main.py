from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/user/<name>')
def get_user(name: str) -> str:
    return f"Hello '{name}'"


if __name__ == '__main__':
    app.run(debug=True)