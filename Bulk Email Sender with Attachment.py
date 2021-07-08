import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from string import Template
import pandas as pd

e = pd.read_csv("FILE_NAME.csv")
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.starttls()
server.login('YOUREMAIL@gmail.com','YOURPASSWORD')

body = ("""
Hi there

This is the body of the email

Thank you
""")
subject = "This is the subject of the email"
fromaddr='abc@gmail.com'
for index, row in e.iterrows():
    print (row["EMAIL_COLUMN_NAME"]+row["ATTACHMENT_COLUMN_NAME"])
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    filename = row["ATTACHMENT_COLUMN_NAME"]
    toaddr = row["EMAIL_COLUMN_NAME"]
    attachment = open(row["ATTACHMENT_COLUMN_NAME"], "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

print("Emails sent successfully")

server.quit()
