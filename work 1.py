import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Add this at the top of your script, after any imports
with open(r"C:\Users\ryku0\Desktop\python\log.txt", "a") as log_file:
    from datetime import datetime
    log_file.write(f"Script ran at {datetime.now()}\n")

# Your existing code continues below...

EMAIL_ADDRESS = "intern@alienlogistics.com"
EMAIL_PASSWORD = "ysOEwioQZ"
SMTP_SERVER = "mail.alienlogistics.com"
SMTP_PORT = 587

TO_EMAILS = [
    "ryku008@gmail.com",
    "ambercoolguy69@gmail.com",
    "-"
]
SUBJECT = "TEST EMAIL ONLY"
BODY = "This email is written in python to test that everything works properly and can be implemented smoothly"

def send_email():
    try:
        print(f"Connecting to {SMTP_SERVER}:{SMTP_PORT}...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.set_debuglevel(1)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        for recipient_email in TO_EMAILS:
            print(f"Sending email to {recipient_email}...")
            msg = MIMEMultipart()
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = recipient_email  # Single recipient
            msg["Subject"] = SUBJECT
            msg.attach(MIMEText(BODY, "plain"))
            
            server.send_message(msg)
            print(f"✅ Email sent to {recipient_email}")

        server.quit()
        print("✅ All emails sent successfully!")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")

send_email()