from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/api/data')
def get_data():
    data = {
        'name': 'John Doe',
        'age': 30
    }
    return data

if __name__ == '__main__':
    app.run(debug=True)
