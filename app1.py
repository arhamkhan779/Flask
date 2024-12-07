from flask import Flask

'''
Creating a app object of flas application
'''
app=Flask(__name__)


''' Decorator it will take two arguments , rule and options'''
@app.route('/')
def welcome():
    return "Welocme to my flask app"


if __name__ == "__main__":
    '''Running the object app , set debug = True'''
    app.run(debug=True)  