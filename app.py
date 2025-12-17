from flask import Flask, render_template
from forms import ContactForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "twoj-sekretny-klucz-123456"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        print(form.name.data, form.email.data, form.message.data)
        return render_template("thank_you.html")

    return render_template("contact.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
