from flask import Flask , render_template , request , make_response , redirect

app = Flask(__name__)

@app.route("/")
def welcome() :    
    return render_template("welcome.html")

        