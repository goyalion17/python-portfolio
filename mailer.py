import os
import smtplib
from email.message import EmailMessage


def mail_configured():
    return all(os.environ.get(k) for k in ("MAIL_USER", "MAIL_PASSWORD"))


def send_contact_message(name, email, message):
    """Send the visitor's message to my own inbox. Raises on SMTP errors."""
    user = os.environ["MAIL_USER"]
    msg = EmailMessage()
    # No line breaks in header values, otherwise someone could inject extra headers
    safe_name = " ".join(name.split())
    msg["Subject"] = f"Portfolio message from {safe_name}"
    msg["From"] = user
    msg["To"] = os.environ.get("MAIL_TO") or user
    msg["Reply-To"] = email
    msg.set_content(f"From: {safe_name} <{email}>\n\n{message}")

    host = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
    port = int(os.environ.get("MAIL_PORT", "587"))
    with smtplib.SMTP(host, port, timeout=10) as smtp:
        smtp.starttls()
        smtp.login(user, os.environ["MAIL_PASSWORD"])
        smtp.send_message(msg)
