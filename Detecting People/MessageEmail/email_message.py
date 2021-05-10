import smtplib,ssl
from twilio.rest import Client

def email_send():
    smtp_server="smtp.gmail.com"
    sender_email="Sender Email"
    receiver_email="Reciever Email"
    port=535
    password='Sender Password'
    message="""
    Subject:Voialation of Social Distancing
    Respected Sir,
          This is a mail to inform you that the social distancing is being hampered in lift.
    """
    context=ssl.create_default_context()
    server=smtplib.SMTP_SSL(smtp_server,port,context=context)
    server.login(sender_email,password)
    server.sendmail(sender_email,receiver_email,message)
def send_message():
    account_sid = 'Account Sid'
    auth_token = 'Auth Token'              #message feature won't work as I had published this publically
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="Social Distancing is hampered.Please have a look!",
                     from_='Sender No',
                     to='Receiver No'
                 )

    print(message.sid)
        
