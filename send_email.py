import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_from = 'email to send from'
email_to = 'email to send to'
password = 'password for email account to send'

msg = MIMEMultipart()

msg['From'] = email_from
msg['To'] = email_to
msg['Subject'] = 'Testing Subject'

body = 'This is the body of the message'
msg.attach(MIMEText(body,'plain'))

filename = 'path to file'
attachment = open(filename, 'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename= '+filename)

msg.attach(part)
text = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls() 
server.login(email_from, password)

server.sendmail(email_from ,email_to, text)
server.quit() 