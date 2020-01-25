##################################################
#  Facade Pattern
##################################################

'''
structure
'''

# The facade pattern is designed to provide a simple interface to a complex system of
# components. For complex tasks, we may need to interact with these objects directly,
# but there is often a "typical" usage for the system for which these complicated
# interactions aren't necessary.
# The facade pattern allows us to define a new object that encapsulates this typical usage of the system
# facade is like an adapter, difference is facade is trying to abstract a simpler interface out of a complex one while adapater is mapping one to another 

# provide an unified interface 
# higher level interface to reduce complexity 

'''
example write a email tool
'''

# the underlying python libraries are very complex 
# facade performs two tasks - 1) sending an email to a specific address 2) checking the inbox on a connection
import smtplib 
import imaplib 

class EmailFacade:
    def __init__(self, host, username, password):
        self.host = host 
        self.username = username 
        self.password = password 
    
    # send_email method formats the email and sends it using smtplib
    def send_email(self, to_email, subject, message):
        if not "@" in self.username:
            from_email = "{0}@{1}".format(
                self.username, self.host)
        else:
            from_email = self.username

        message = ("From: {0}\r\n"
                "To: {1}\r\n"
                "Subject: {2}\r\n\r\n{3}").format(
                from_email,
                to_email,
                subject,
                message)
        smtp = smtplib.SMTP(self.host)
        smtp.login(self.username, self.password)
        smtp.sendmail(from_email, [to_email], message)

    def get_inbox(self):
        mailbox = imaplib.IMAP4(self.host)
        mailbox.login(bytes(self.username, 'utf8'),
            bytes(self.password, 'utf8'))
        mailbox.select()
        x, data = mailbox.search(None, 'ALL')
        messages = []
        for num in data[0].split():
            x, message = mailbox.fetch(num, '(RFC822)')
            messages.append(message[0][1])
        return messages 

'''
example - pull records 
'''
# def get_employees():
#     connection = connect()
#     query = '''
#     '''
#     cursor = connection.cursor()
#     # ...
#     connection.commit()
#     connection.close()


