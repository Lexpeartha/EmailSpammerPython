from email.message import EmailMessage
import smtplib
import random as r

EMAIL = "yourmail@gmail.com" # This method only works with Gmail
PASSWORD = "unbreakablepassword" # You will need to allow external apps to access your account in the settings too
TIMES_TO_SEND_MAIL = 250

# Just write your spammy message here or whatever
message = """
Add any spammy text you want here!
"""

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
