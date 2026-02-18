Automated Clinic Token & Availability Management System
📌 Project Overview

The Automated Clinic Token & Availability Management System is a web-based application designed to digitalize and automate OPD queue management in clinics and hospitals.
It replaces manual token systems with a smart, real-time platform that manages patient tokens based on doctor availability and session capacity.

🚀 Features

User Authentication (Admin, Doctor, Patient)

Secure login with password hashing

Dynamic token handling system

Role-based dashboards

Session management

SQLite database integration

Responsive frontend UI

🧠 Problem Statement

Traditional OPD systems rely on manual token allocation which results in:

Long waiting times

Overcrowding

Poor time management

Appointment cancellations

Lack of real-time updates

💡 Solution

This system automates OPD management by:

Digitally assigning tokens

Managing doctor availability

Providing real-time dashboards

Ensuring secure authentication

Reducing manual errors

🏗️ Project Structure
Enkryptia_zip/
│
├── app.py                 # Main Flask backend
├── database.db            # SQLite database
│
└── Enkryptia/
    ├── templete/          # HTML templates
    │     ├── admin.html
    │     ├── doctor.html
    │     ├── patient.html
    │     ├── login.html
    │     ├── homepage.html
    │     ├── signuppage.html
    │     └── others...
    │
    └── static/            # CSS/JS files (if added)

⚙️ Tech Stack

Frontend

HTML

CSS

JavaScript

Backend

Python Flask

Database

SQLite

Security

Werkzeug password hashing

🔐 Authentication System

Users register with:

Username

Password

Role (Admin / Doctor / Patient)

Passwords are securely stored using hashing.

🖥️ Dashboards

Different dashboards are provided based on role:

Role	Access
Admin	Full system management
Doctor	Doctor dashboard
Patient	Patient dashboard
🗄️ Database Schema
Users Table
Column	Type
id	Integer
username	Text
password	Text
role	Text
▶️ How to Run the Project
1️⃣ Install Dependencies
pip install flask werkzeug

2️⃣ Run Server
python app.py

3️⃣ Open Browser
http://127.0.0.1:5000

🔁 System Workflow

User registers account

User logs in

System verifies credentials

Redirects to role dashboard

User performs actions

📈 Future Enhancements

Live token tracking

SMS/WhatsApp notifications

AI patient flow prediction

Online appointment booking

Mobile app version

Doctor leave auto-handling

Real-time queue dashboard

🎯 Innovation

Unlike traditional appointment systems, this project focuses on:

Real-time availability

Automated scheduling logic

Dynamic token generation

Role-based access system

🧪 Testing

Test cases include:

Login validation

Role authorization

Database insertion

Session handling

👨‍💻 Author

Project Name: Enkryptia – Smart OPD Manager
Developed by: TEAM AVICTRON

📜 License

This project is developed for educational and academic purposes.
