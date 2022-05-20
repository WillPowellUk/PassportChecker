import smtplib
import yaml
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


class EmailSender:
  def __init__(self):
      pass

  def send(self, emailReceivers, senderName, subject, message):
    # load login details from text file
    conf = yaml.safe_load(open('loginDetails.yml'))
    myGmail = conf['gmail_login']['email']
    myGmailPassword = conf['gmail_login']['password']

    for emailReceiver in emailReceivers:
      # Define the source and target email address.
      emailSender = myGmail
      # Create an instance of MIMEMultipart object, pass 'related' as the constructor parameter.
      msgRoot = MIMEMultipart('alternative')
      # Set the email subject.
      msgRoot['Subject'] = subject
      # Set the email from email address.
      msgRoot['From'] = senderName
      # Set the email to email address.
      msgRoot['To'] = emailReceiver
      # Set message
      msgRoot.attach(MIMEText(message, 'plain'))

      # Set the multipart email preamble attribute value. Please refer https://docs.python.org/3/library/email.message.html to learn more.
      msgRoot.preamble = '====================================================='

      # Send Email
      conn = smtplib.SMTP('smtp.gmail.com', 587)  # smtp address and port
      conn.ehlo()  # call this to start the connection
      conn.starttls()  # starts tls encryption. When we send our password it will be encrypted.
      conn.login(myGmail, myGmailPassword)
      conn.sendmail(emailSender, emailReceiver, msgRoot.as_string())
      conn.quit()
    print("message sent")
