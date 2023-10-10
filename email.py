import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import json
import time

# The mail addresses and password
sender_address = ''
sender_pass = ''
# Setup the MIME

# fetch email into this dynamic list
r = open("src/New_folder/csvjson.json",)
# r = open("src/New_folder/main.json",)
reciepents = json.load(r)
r.close()
lst = open(r"lst.json")


# starting session
session = smtplib.SMTP('smtp.mail.yahoo.com', 587)
# starting secure login
session.starttls()
# logging in
session.login(sender_address, sender_pass)


# this function sends the email
def sendmail(sender_address, receiver_address, subject, content, receiver_name, receiver_id):
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    # The subject line

    message['Subject'] = subject

    # The body and the attachments for the mail
    message.attach(MIMEText(content, 'plain'))
    attach_file_name = 'src/New_folder/certificates/' + str(i+1)+'.png'
    with open(attach_file_name, 'rb') as f:
        img_data = f.read()

    image = MIMEImage(img_data, name=os.path.basename(attach_file_name))
    message.attach(image)
    print("image attached! with name: " + str(i+1))

    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)

    print(f"Mail Sent to {receiver_name} + " + str(i))


subject = "Agenda✨"


def func_content_final(content):
    greeting = "Hello " + reciever_name + ",\n"
    signature = "\n\nThank you \nfor subscribe us"
    content_ = greeting + content + signature
    return content_

def making_listToJson():
            res = []
            for i in range(1,69):
                temp = {"name": reciever_name[i+1],
                    "email": sender_address[i]}
                res.append(temp)
                print(res)
                jsonFile = open("lst.json", "w")
                jsonFile.write(json.dumps(res))
                jsonFile.close()


# for sending mails in a loop
for i in range(166, 167):
    content = '''you will get Update about our upcoming event.'''
    reciever_name = reciepents[i]["name"]
    content_final = func_content_final(content)
    sendmail(sender_address, reciepents[i]["email"],
            subject, content_final, reciever_name, i+1)

    print(f'sent to {reciepents[i+1]["name"]}')




