from flask import Flask

app=Flask(__name__)

@app.route('/')
def welocome():
    return "Welcome to my second app"

@app.route('/Firstapp')
def welcome_other():
    return "Welcome to my first app"

if __name__ == "__main__":
    app.run(debug=True)