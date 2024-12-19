'''
Integrating Flask with HTML
HTTP Verbs GET POST 
'''

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template("home.html")

@app.route('/form')
def form():
    return render_template("index.html")

@app.route('/success/<float:score>')
def results(score):
    res=""
    if score >= 50:
        res="Pass"
    else:
        res="Fail"
    return render_template("results.html",result=res,percentage=score)


@app.route("/submit",methods=['GET','POST'])
def submit():
    total_score=0
    if request.method == "POST":
        science_marks=float(request.form['science'])
        maths_marks=float(request.form['maths'])
        c_marks=float(request.form['c'])
        data_science_marks=float(request.form['datascience'])
        total_score=(science_marks+maths_marks+c_marks+data_science_marks)/4
    res="results"
    return redirect(url_for(res,score=total_score))


if __name__ == "__main__":
    app.run(debug=True)