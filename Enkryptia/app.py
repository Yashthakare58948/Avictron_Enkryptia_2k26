from flask import Flask, render_template, request, jsonify, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__, template_folder='Enkryptia/templete', static_folder='Enkryptia/static')
app.secret_key = "enkryptia_secret_key"

# Database file path
DB_PATH = "database.db"

# ---------------- DATABASE INIT ----------------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------------- ROUTES ----------------
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/loginpage")
def login_page():
    return render_template("login.html")

@app.route("/signuppage")
def signup_page():
    return render_template("signuppage.html")

# ---------------- SIGNUP ----------------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    username = data["username"]
    password = generate_password_hash(data["password"])
    role = data["role"]

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
            (username, password, role)
        )
        conn.commit()
        conn.close()
        return jsonify({"status": "success"})
    except:
        return jsonify({"status": "exists"})

# ---------------- LOGIN ----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data["username"]
    password = data["password"]
    role = data["role"]

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password FROM users WHERE username=? AND role=?",
        (username, role)
    )
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user[0], password):
        session["user"] = username
        session["role"] = role
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "fail"})

# ---------------- DASHBOARDS ----------------
@app.route("/doctor")
def doctor():
    if session.get("role") == "doctor":
        return render_template("doctor.html")
    return redirect("/loginpage")

@app.route("/patient")
def patient():
    if session.get("role") == "patient":
        return render_template("patient.html")
    return redirect("/loginpage")

@app.route("/admin")
def admin():
    if session.get("role") == "admin":
        return render_template("admin.html")
    return redirect("/loginpage")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
