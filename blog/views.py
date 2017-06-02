from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    #return 'Hello World!'

    MyList = [1, 2, 3]
    return render_template("index.html", message="Hello World!, I have been passed as a context.", data=MyList)

    #return render_template("index.html", data=MyList)

@app.route('/about')
def about():
    return('The about page')
