import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    port = os.environ.get("PORT") or 5000
    app.run("0.0.0.0", port)
