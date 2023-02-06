# from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.application import MIMEApplication
import smtplib

def sendmail(user, pwd, receiver, subject, body, path):
    # setup the message
    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = receiver
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    # block of code for images archives
    '''# add file to the message
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # encode the base64
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={filename}")
    msg.attach(part)'''

    # block of code for pdf archives
    with open(path, "rb") as attachment:
        part = MIMEApplication(attachment.read(),_subtype="pdf")
    part.add_header("Content-Disposition", "attachment", filename=str(path))
    msg.attach(part)


    try:
        # setup the SMTP server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, pwd)
        server.sendmail(user, receiver, msg.as_string())
        server.close()
        print("\033[33mEmail has been successfully sent!\033[m")
        return True
    except Exception as e:
        print("Something went wrong: " + str(e))
        return False
