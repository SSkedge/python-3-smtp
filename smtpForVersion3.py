import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# @author Steven Skedge
# Date: 16/02/2017
# SMTP Tester
# Requires:
# -Host
# -From Email/Username
# -To Email
# -Password

msg = MIMEMultipart()
msg['From'] = '<from:email>'
msg['To'] = '<to:email>'
msg['Subject'] = 'SMTP Tester'
message = 'Test Email!'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('<host>',<port>)

mailserver.ehlo()

mailserver.starttls()

mailserver.ehlo()
mailserver.login('<from:email>', '<password>')

try:
    mailserver.sendmail('<from:email>','<to:email>',msg.as_string())
    print('Email sent to %s successfully' % (msg['To']))
except smtplib.SMTPException:
    print('Something went wrong while trying to send to %s' % (msg['To']))
mailserver.quit()
