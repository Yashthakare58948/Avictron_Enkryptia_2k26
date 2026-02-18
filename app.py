
from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import smtplib
from email.mime.text import MIMEText
import random
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("clinic.db")
    conn.row_factory = sqlite3.Row
    return conn

# ---------- HOME ----------
@app.route("/")
def home():
    return render_template("index.html")

# ---------- REAL-TIME TV MODE ----------
@app.route("/tv")
def tv():
    return render_template("tv.html")

@app.route("/current_token")
def current_token():
    conn = get_db()
    token = conn.execute("SELECT token_number FROM appointments WHERE status='Waiting' ORDER BY token_number LIMIT 1").fetchone()
    conn.close()
    if token:
        return jsonify({"token": token["token_number"]})
    return jsonify({"token": "None"})

# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    conn = get_db()
    total = conn.execute("SELECT COUNT(*) FROM appointments").fetchone()[0]
    waiting = conn.execute("SELECT COUNT(*) FROM appointments WHERE status='Waiting'").fetchone()[0]
    completed = conn.execute("SELECT COUNT(*) FROM appointments WHERE status='Completed'").fetchone()[0]
    conn.close()
    return render_template("dashboard.html", total=total, waiting=waiting, completed=completed)

# ---------- BOOK ----------
@app.route("/book", methods=["GET","POST"])
def book():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        date = request.form["date"]

        conn = get_db()
        count = conn.execute("SELECT COUNT(*) FROM appointments WHERE date=?", (date,)).fetchone()[0]
        token = count + 1

        conn.execute("INSERT INTO appointments (patient_name, email, date, token_number, status) VALUES (?,?,?,?,?)",
                     (name, email, date, token, "Waiting"))
        conn.commit()
        conn.close()

        send_email(email, token)

        return render_template("success.html", token=token)

    return render_template("book.html")

# ---------- EMAIL ----------
def send_email(receiver, token):
    try:
        msg = MIMEText(f"Your Token Number is {token}")
        msg["Subject"] = "Clinic Appointment Token"
        msg["From"] = "your_email@gmail.com"
        msg["To"] = receiver

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("your_email@gmail.com", "your_app_password")
        server.send_message(msg)
        server.quit()
    except:
        pass

# ---------- AI PREDICTION ----------
@app.route("/predict")
def predict():
    X = np.array([[1],[2],[3],[4],[5]])
    y = np.array([5,7,9,11,13])
    model = LinearRegression()
    model.fit(X,y)
    prediction = model.predict([[6]])
    return f"Predicted Future Appointments: {int(prediction[0])}"

if __name__ == "__main__":
    app.run(debug=True)
