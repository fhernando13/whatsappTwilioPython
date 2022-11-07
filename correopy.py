#not named file "email.py"
import os
from dotenv import load_dotenv
import smtplib 
from email.message import EmailMessage 

email_subject = "Title email"
sender_email_address = "from_mail@email.com"
receiver_email_address = "to_mail@email.com"
another_email_address = "cc_mail@email.com"
load_dotenv()
email_smtp = os.getenv('mail.mail.com')
email_password = os.getenv('EMAIL_PASSWORD')

message = EmailMessage() 
message['Subject'] = email_subject 
message['From'] = sender_email_address 
message['To'] = receiver_email_address 
message['CC'] = another_email_address
message.set_content("Hello from Python!") 
server = smtplib.SMTP(email_smtp, '587') 
server.ehlo() 
server.starttls() 
# server.is_ssl()
server.login(sender_email_address, email_password) 
server.send_message(message) 
server.quit()
