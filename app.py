from flask import Flask, render_template, request, flash

# initialize app
app = Flask(__name__)

app.secret_key = 'secret_key'

# renders the default page
@app.route("/")
def index():
    markers = [-75.480858, 40.632950]
    return render_template("index.html", markers=markers)