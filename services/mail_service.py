import os
from flask_mail import Mail, Message
from flask import render_template

mail = Mail()

def send_welcome_email(app, username, email):
    """Send a welcome email to a newly registered user."""
    try:
        app_url = os.environ.get("APP_URL", "http://localhost:5000")
        with app.app_context():
            msg = Message(
                subject="🕉 Welcome to KrishnAI — Your Journey Begins",
                sender=os.environ.get("MAIL_DEFAULT_SENDER", "noreply@krishnai.com"),
                recipients=[email]
            )
            msg.html = render_template(
                "email_welcome.html",
                username=username,
                app_url=app_url
            )
            mail.send(msg)
    except Exception as e:
        # Never let email failure break signup
        print(f"[Mail] Failed to send welcome email to {email}: {e}")
