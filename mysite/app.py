from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def principal.html():
    return render_template("principal.html")