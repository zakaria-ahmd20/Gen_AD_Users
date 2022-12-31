import  os
import ssl
import smtplib
import csv
from email.message import EmailMessage
with open("users.csv", 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader) # removes header as we need raw data
  for row in csvreader: # loops through CSV file
    username = (f"{row[0]}.{row[1]}")
    passcode = (row[2])
    email_reciever = (row[4])
    email_password = os.environ.get('EMAIL_PASSWORD') # windows env variable
    email_sender = 'youremail@yourserver.com'
    subject = f"{username}'s crediantls"
    body = f" Hi here is the credentails for your new onboarding username is {username},password is {passcode} " 
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_reciever
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.yourserver.com',465,context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender,email_reciever,em.as_string())
