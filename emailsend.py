from smtplib import SMTP
def send_email(sender, receiver, )
sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""

with SMTP("smtp.gmail.com", 465) as smtp:
    smtp.sendmail(from_addr='from@address.com', to_addrs=['to@address.com'], msg = "This message")
    smtp.quit()