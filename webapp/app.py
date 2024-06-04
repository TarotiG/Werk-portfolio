from flask import Flask, render_template
from scripts.coconuts import get_coconuts


app = Flask(__name__)
coconuts = get_coconuts()

@app.route("/")
def homepage():
    return render_template(
        "home.html",
        COCONUTS=coconuts
    )

@app.route("/contact")
def contact():
    return render_template(
        "contact.html"
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        debug=True
    )