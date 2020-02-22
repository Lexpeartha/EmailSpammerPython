from email.message import EmailMessage
import smtplib
import random as r

EMAIL = "yourmail@gmail.com" # This method only works with Gmail
PASSWORD = "unbreakablepassword" # You will need to allow external apps to access your account in the settings too
TIMES_TO_SEND_MAIL = 250

# Just write your spammy message here or whatever
message = """
No place can inspire incredible stories quite like Orlando. It’s a destination filled with wonder and adventure, where children and grownups alike can let their imagination soar. A place where you can reconnect with what matters most and fill your days with one-of-a-kind experiences you’ll never forget. A city built on magic and dreams — and now, we want to bring you and your family to Orlando as our guest for the vacation of a lifetime.

Simply complete the form below, and you’ll be entered to win a dream vacation for four to the most visited tourism destination in the U.S.

The winner will receive:

    Round trip airline tickets to Orlando for winner and up to three (3) guests.
    Four night stay at Lake Buena Vista Resort Village & Spa in a two bedroom/two bath suite including a $100 Reflections Spa & Salon gift certificate.
    Eight (8) single-day theme park tickets to your choice of Walt Disney World Resort or SeaWorld Orlando
    Full-size rental vehicle for five (5) days provided by Enterprise Rent-a-Car

It’s your chance to create your own Orlando story — one that will live on long after your vacation draws to a close, told through wide smiles, heartwarming joy and priceless memories. Enter now to take the first steps toward making your Orlando dreams come true!"""

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL, PASSWORD)
    for _ in range(TIMES_TO_SEND_MAIL):
        msg = EmailMessage()
        # To seperate emails and make it look spammy, I'm changing dynamically Subject of mail by adding random number to it
        # This is not necessary tho
        luckyWinner = r.randint(85, 835)
        msg.set_content(message)
        SUBJECT = "Win the Orlando Family Vacation, You Are Lucky Winner Number #" + str(luckyWinner)
        msg['Subject']= SUBJECT
        msg['From'] = EMAIL
        msg['To'] = ['miroslava.nikolic65@gmail.com']
        smtp.send_message(msg)
        msg.__delitem__ # Removes msg's parameters so it can change them again in next loop cycle