from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    #return 'Hello World!'

    #### PASSING CONTEXT TO TEMPLATE PAGES #####
    mymessage = 'Hello World!, I have been passed as a context.'
    mylist = [1, 2, 3]
    mydictlist = [{"name": 'Jason'}, {"name": 'Alice'}, {"name": 'Lucy'}]
    # return render_template("index.html", mymessage=mymessage, mylist=mylist, mydictlist=mydictlist)


    #### 2) GET POST METHODS ####
    # the default method is GET
    getpostmessage = "This is a GET request"
    if request.method == "POST":
        getpostmessage="This is a POST request"

    return render_template("index.html", mymessage=mymessage, mylist=mylist, \
                           mydictlist=mydictlist, getpostmessage=getpostmessage)

@app.route('/about')
def about():
    return('The about page')

#### 3) DYNAMIC URL ####
@app.route('/about/<varurl>')
def dynamicurl(varurl):
    return('This page is  about {0}.'.format(varurl))
