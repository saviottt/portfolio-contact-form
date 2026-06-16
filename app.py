from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    email_content = f"""
    New Portfolio Contact Submission

    Name: {name}
    Email: {email}
    Message: {message}
    """

    send_email("New Message from Your Portfolio", email_content)
    return render_template("index.html", success_message="Thanks for contacting me!")

def send_email(subject, body):
    sender_email = os.getenv("EMAIL_USER")
    receiver_email = "donsavio1one@gmail.com"
    app_password = os.getenv("EMAIL_PASSWORD")
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

