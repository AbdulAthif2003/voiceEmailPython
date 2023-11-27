from talk import talk
import email
import imaplib
from send_email import send_email
from information import get_info

email_list = {
    'ak': 'ashokmithra02072003@gmail.com',
    'bk': 'aashokmithra4@gmail.com',
    'ck': 'abdulathif9080485766@gmail.com'

}

# To Whom you want to send email


def get_email_info():
    print('Hello Sir I am your assistant for today')
    talk('Hello Sir I am your assistant for today')
    print('You are loggend into your email Choose the option')
    talk('You are loggend into your email Choose the option')
    print('1. Compose Mail')
    talk('1. Compose Mail')
    print('2. Check your inbox')
    talk('2. Check your inbox')
    print('Choose your option')
    talk('Choose your option')
    text = get_info()
    if text == '1' or text == '11' or text == 'one' or text == "one one":
        talk('To whom you want to send email')
        name = get_info()
        receiver = email_list[name]
        print(receiver)
        talk('What is the subject of your email?')
        subject = get_info()
        talk('Tell me the text in your email')
        message = get_info()
        send_email(receiver, subject, message)
        talk('Thankyou sir for using me. Your email has been send')
        talk('Do you want to send more email?')
        send_more = get_info()
        if (send_more is None):
            talk('Thank you sir for using me')
        elif 'yes' in send_more:
            get_email_info()
        else:
            talk('Thank you sir for using me')

    elif text == '2' or text == "22" or text == 'tu' or text == 'tu tu' or text == 'two' or text == 'to' or text == "two two":
        server = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    server.login('abdulathif9080485766@gmail.com','lldxhcznnvlzvxde')

    print('Select the choice from the inbox')
    talk('Select the choice from the inbox')
    print('1 latest emails received')
    talk('1 latest emails received')
    print('2 unseen emails')
    talk('2 unseen emails')
    print('Choose your option')
    talk('Choose your option')
    response = get_info()

    if response == '1' or response == 'one' or response == '11' or response == 'one one':
        status, messages = server.select('Inbox')
        print(str(messages))
    elif response == '2' or response == '22' or response == 'tu' or response == 'two' or response == 'tu tu' or response == 'two two' or response == 'to' or response == "to to":
        status, messages = server.select(None, 'Unseen')

    N = 1
    messages = int(messages[0])

    for i in range(messages, messages-N, -1):
        # fetch the email message by ID
        res, msg = server.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject = msg["Subject"]
                # decode email sender
                From = msg.get("From")

                print("From:", From)
                talk('From '+From)

                print("Subject:", subject)
                talk('Subject:'+subject)
                # if the email message is multipart
                if msg.is_multipart():
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        print(content_type)
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain":
                            print(body)
                            talk(body)
                else:
                    content_type = part.get_content_type()
                    if content_type == "text/plain":
                        print(body)
                        talk(body)

                print("="*100)
    print('Thank you sir for using me')
    talk('Thank you sir for using me')


get_email_info()
