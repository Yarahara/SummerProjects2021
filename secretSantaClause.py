#credit to lena elizabeth on Youtube

import random
import smtplib

# list of people

people=['alice@gmail.com', 'bob@gmail.com', 'charlie@gmail.com', 'diane@gmail.com', 'edward@gmail.com']

#re-ordering of the list to be random

random.shuffle(people)

draw = {}
for i in range(len(people)):
    if i == len(people) - 1:
        draw[people[i]] = people[0]
    else:
        draw[people[i]] = people[i+1]

print(draw)

#email-sending program

sender = input("Type your email and press enter: ")
password = input("Type your gmail password and press enter: ")

for (gift_giver, reciever) in draw.items():
'''
#testing with single email
gift_giver = '...@gmail.com'
receiver = 'mom'
'''
    try:
        gift_givers = [gift_giver]

        #the message variable of the email
        message = f"""
        Hello {gift_giver}
        Your secret santa is: {reciever}
        """

        #sets up the session for sending the email
        session = smtplib.SMTP('smtp.gmail.com' 587)
        session.enlo()
        session.starttls()
        session.enlo()
        session.login(sender,password)
        session.sendmail(sender, gift_givers, message) #sends from sender to gift giver with message
