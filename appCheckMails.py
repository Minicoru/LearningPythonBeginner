# import imaplib
# import getpass
# import email
#
# #login to gmail
# mail = imaplib.IMAP4_SSL('imap.gmail.com')
# #mail.login('<username>', '<password>')
# #mail.login('miarg49@gmail.com', 'SilverGod_x2080,.')
# mail.login(getpass.getuser(), getpass.getpass())
#
# #select the inbox mail box
# mail.select("inbox")
#
# #search mails
# result, data = mail.search(None, "ALL")
#
# #get the list of ids of the mails
# ids = data[0]
#
# #split the ids of the mails
# id_list = ids.split()
#
# #iterate over each mail
# for num in data[0].split():
#     typ, data = mail.fetch(num, '(RFC822)')
#     raw_email = data[0][1]
#
#     #convert the raw email to message object
#     email_message = email.message_from_string(raw_email)
#     # get the subject
#     email_subject = email_message['Subject']
#     # get the body
#     email_body = email_message.get_payload()
#     # check if the mail has the keyword desubscribe
#     if "desubscribe" in email_body:
#         mail.store(num, '+X-GM-LABELS', '\\Spam')
#     if "unsubscribe" in email_body:
#         mail.store(num, '+X-GM-LABELS', '\\Spam')
#     if "desuscribir" in email_body:
#         mail.store(num, '+X-GM-LABELS', '\\Spam')
#     if "suscribe" in email_body:
#         mail.store(num, '+X-GM-LABELS', '\\Spam')
#
# #close the connection to the mail
# mail.close()
# mail.logout()


import oauth2 as oauth
import oauth2.clients.imap as imaplib

# Set up your Consumer and Token as per usual. Just like any other
# three-legged OAuth request.
consumer = oauth.Consumer('your_consumer_key', 'your_consumer_secret')
token = oauth.Token('your_users_3_legged_token',
    'your_users_3_legged_token_secret')

# Setup the URL according to Google's XOAUTH implementation. Be sure
# to replace the email here with the appropriate email address that
# you wish to access.
url = "https://mail.google.com/mail/b/miarg49@gmail.com/imap/"

conn = imaplib.IMAP4_SSL('imap.googlemail.com')
conn.debug = 4

# This is the only thing in the API for impaplib.IMAP4_SSL that has
# changed. You now authenticate with the URL, consumer, and token.
conn.authenticate(url, consumer, token)

# Once authenticated everything from the impalib.IMAP4_SSL class will
# work as per usual without any modification to your code.
conn.select('INBOX')
print(conn.list())