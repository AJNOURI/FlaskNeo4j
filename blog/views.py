from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello():
    #return 'Hello World!'
    mymessage = 'Hello World!, I have been passed as a context.'
    mylist = [1, 2, 3]
    mydictlist = [{"name": 'Jason'}, {"name": 'Alice'}, {"name": 'Lucy'}]
    return render_template("index.html", mymessage=mymessage, mylist=mylist, mydictlist=mydictlist)


@app.route('/about')
def about():
    return('The about page')
