
##################################################
# Email
##################################################

'''
send email message
'''
# https://pymotw.com/3/smtplib/index.html

import smtplib
import email.utils 
from email.mime.text import MIMEText

msg = MIMEText('This is the email body')
msg['To'] = email.utils.formataddr(('Recipient',
                                    'recipient@example.com'))
msg['FROM'] = email.utils.formataddr(('Author',
                                      'author@example.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('localhost', 1025)
server.set_debuglevel(True)
try:
    server.sendmail('author@example.com',
                    ['recipient@example.com'],
                    msg.as_string())
finally:
    server.quit()


'''
authentication and encryption
'''
# Use TLS (transport layer security) encryption
server = smtplib.SMTP_SSL(servername, serverport)
# Insecure connection
smtplib.SMTP(servername, serverport)


