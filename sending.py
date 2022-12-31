def email_credentials():
  import  os
  import ssl
  import smtplib
  import csv
  from email.message import EmailMessage
  with open("users.csv", 'r') as file:
    csvreader = csv.reader(file)
    next(csvreader)
    for row in csvreader:
      username = (f"{row[0]}.{row[1]}")
      passcode = (row[2])
      email_reciever = (row[4])
      email_password = os.environ.get('EMAIL_PASSWORD')
      email_sender = 'hawkmoonsquad@gmail.com'
      subject = f"{username}'s crediantls"
      body = f" Hi here is the credentails for your new onboarding username is {username},password is {passcode}" \
             f"User will have to change their passcode on the next login" \
             f"This email was auto_generated please do not reply and reach out to your technical specialist for issues "
      em = EmailMessage()
      em['From'] = email_sender
      em['To'] = email_reciever
      em['Subject'] = subject
      em.set_content(body)
      context = ssl.create_default_context()
      with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
          smtp.login(email_sender,email_password)
          smtp.sendmail(email_sender,email_reciever,em.as_string())

      print('succesfully sent out emails')
