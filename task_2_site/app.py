from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", active_page="index")


@app.route("/blog/")
def blog():
    return render_template("blog.html", active_page="blog")


@app.route("/contacts/")
def contacts():
    return render_template("contacts.html", active_page="contacts")


if __name__ == "__main__":
    app.run(debug=True)

