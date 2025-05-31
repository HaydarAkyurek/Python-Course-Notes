import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

# SMTP server configuration
port = 587  # Standard TLS port
smtp_server = "smtp-relay.brevo.com"  # Brevo SMTP server (formerly Sendinblue)
login = "<your_login>"  # Your SMTP login
password = "<your_password>"  # Your SMTP password or API key

# Email addresses and subject
sender_email = "your_email@example.com"  # Sender email address
sender_name = "Your Name"  # Optional sender name
recipient_emails = ["recipient1@example.com", "recipient2@example.com"]  # List of recipient emails
subject = "Hello from Python"

# Email content (both plain text and HTML)
text_content = "Hello,\nThis email was sent from my Python application."
html_content = """
<html>
  <body>
    <p>Hello,<br>
       This email was <b>sent from my Python application</b>.<br>
       Have a nice day!
    </p>
  </body>
</html>
"""

# Create a multipart message and set headers
message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = f"{sender_name} <{sender_email}>"
message["To"] = ", ".join(recipient_emails)

# Attach plain text and HTML parts
part1 = MIMEText(text_content, "plain", "utf-8")
part2 = MIMEText(html_content, "html", "utf-8")
message.attach(part1)
message.attach(part2)

# Send the email
try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # Secure the connection with TLS
        server.login(login, password)  # Log in to the SMTP server
        server.sendmail(sender_email, recipient_emails, message.as_string())  # Send the message
    print("Email sent successfully.")
except Exception as e:
    print("An error occurred while sending the email:", e)
    sys.exit(1)
