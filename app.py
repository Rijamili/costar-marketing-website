from flask import Flask, render_template, request, redirect, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ---------------- CONFIG ----------------

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SECRET_KEY"] = "secret"

db = SQLAlchemy(app)


# ---------------- DATABASE MODEL ----------------

class Lead(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(50))
    message = db.Column(db.Text)


# ---------------- HOME ROUTES ----------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/books")
def books():
    return render_template("books.html")


@app.route("/company")
def company():
    return render_template("company.html")


# ---------------- CONTACT FORM ----------------

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        new_lead = Lead(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        db.session.add(new_lead)
        db.session.commit()

        return redirect("/dashboard")

    return render_template("contact.html")


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "1234":
            session["admin"] = True
            return redirect("/dashboard")

    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    if not session.get("admin"):
        return redirect("/login")

    leads = Lead.query.all()

    return render_template("dashboard.html", leads=leads)

@app.route("/delete/<int:id>")
def delete_lead(id):

    if not session.get("admin"):
        return redirect("/login")

    lead = Lead.query.get(id)

    db.session.delete(lead)
    db.session.commit()

    return redirect("/dashboard")


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect("/")


# ---------------- CREATE DATABASE ----------------

@app.route("/createdb")
def createdb():

    db.create_all()

    return "Database Created Successfully"


# ---------------- SIMPLE CHATBOT ----------------

@app.route("/chatbot", methods=["POST"])
def chatbot():

    data = request.get_json()

    message = data.get("message", "").lower()

    if "price" in message or "consultation" in message:
        reply = "Our consultancy fee starts from $1000."

    elif "services" in message:
        reply = "We provide SEO, Social Media Marketing, and Digital Consultancy."

    elif "contact" in message:
        reply = "You can contact us at shibilims007@gmail.com."

    elif "countries" in message:
        reply = "We operate in UAE, India, Sri Lanka, Nepal and Pakistan."

    else:
        reply = "Our team will contact you soon for consultancy."

    return jsonify({"response": reply})


# ---------------- RUN SERVER ----------------

if __name__ == "__main__":
    app.run(debug=True)