# modules/send_email.py
from utils.gmail_auth import gmail_login
from email.mime.text import MIMEText
import base64
import logging  #added for logging


def create_message(sender: str, to: str, subject: str, message_text: str):
    message = MIMEText(message_text)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    return {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}

def send_message(service, user_id: str, message: dict):
    try:
        sent_message = service.users().messages().send(userId=user_id, body=message).execute()
        print(f"✅ Message sent! Message ID: {sent_message['id']}")
        return sent_message
    except Exception as error:
        print(f"❌ An error occurred: {error}")
        return None

# def send_email(to: str, subject: str, body: str):
#     service = gmail_login()
#     user = "me"  # Gmail API uses 'me' to refer to authenticated user
#     message = create_message(sender=user, to=to, subject=subject, message_text=body)
#     return send_message(service, user, message)

# Function to send an email using Gmail API
def send_email(to: str, subject: str, body: str):
    try:
        service = gmail_login()
        user = "me"  # Gmail API uses 'me' to refer to authenticated user
        message = create_message(sender=user, to=to, subject=subject, message_text=body)
        response = send_message(service, user, message)
        logging.info(f"Email sent successfully: {response}")
        return True
    except Exception as e:
        logging.error(f"Error sending email: {str(e)}")
        return False

