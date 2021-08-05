from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import config

message = MIMEMultipart()
message["from"] = "Simon Denisov"
message["to"] = 'semsemden@gmail.com'
message["subject"] = "Test"
message.attach(MIMEText("Body"))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("simondnsv@gmail.com", config.password)
    smtp.send_message(message)
    print("Sent...")
