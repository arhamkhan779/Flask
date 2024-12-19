'''
How to Build URL dynamically
Flask variables and URL Builder
app.route(  URL , Methods) --->Decorator
'''

from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my app"

@app.route('/success/<int:score>')
def success(score):
    return f"The Person has Passed and the score is {score}"

@app.route('/fail/<int:score>')
def fail(score):
    return f"The Person has Failed and the score is {score}"

@app.route("/results/<int:marks>")
def results(marks):
    result=""
    if marks >= 50:
       result = "success"
    else:
        result = "fail"
    return redirect(url_for(result,score=marks))

if __name__ == "__main__":
    app.run(debug=True)