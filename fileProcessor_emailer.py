import random
import smtplib
import pandas as pd
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fileProcessor_globals import *

# Removes rows with duplicate emails
def studyfind_removeDupEmails_inPlace(filePath):
  df = pd.read_csv(filePath)
  df.drop_duplicates(subset=['Email'], inplace=True)
  # erases the current content of the file
  file = open(filePath, 'w')
  df.to_csv(filePath, mode='a', index=False)
  file.close()

# Fixes column names to be the expected column names for splitting.
def studyfind_fix_columns(filePath):
    data = pd.read_csv(filePath)
    if (not 'Email' in data.columns):
        data = data.rename(columns={' Contact Email':'Email'})
    if (not 'Name' in data.columns):
        data = data.rename(columns={' Contact Name':'Name'})

# Sends emails from a file
# from_email: email address you are emailing from
# app_password: app password set up on Google accounts
# subject_lines: list of subject lines that will be picked from at random to use
# email_body: body of the email to send
# num_emails: number of emails to send at a time, to avoid spam
def studyfind_sendEmails(filePath, from_email, num_emails=50):
    app_password = EMAIL_DICT[from_email]["app_password"]
    subject_lines = EMAIL_DICT[from_email]["subject_lines"]
    email_body = EMAIL_DICT[from_email]["body"]

    studyfind_removeDupEmails_inPlace(filePath)
    # read data from csv file
    data = pd.read_csv(filePath)
    # create a new column to track the emails
    data["Status"] = "not sent"
    data.to_csv(filePath, index=False)

    # append the data into an array
    names = []
    emails = []
    statuss = []

    for name in data.Name:
        names.append(name)

    for email in data.Email:
        emails.append(email)

    for status in data.Status:
        statuss.append(status)

    # method to check if the data is empty
    def isNaN(string):
        return string != string

    total = len(emails)    

    i = 0
    while i < total:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(from_email, app_password)

        for _ in range(num_emails):
            if (i >= total):
                break

            researcher_email = emails[i]
            researcher_name = names[i]
            # Check if there is a name and email, dont send if there isnt
            if  isNaN(researcher_name)  or  isNaN(researcher_email):
                statuss[i]="no name or no email"
            
            # Any extra clauses here
            # elif researcher_email.endswith("@bu.edu"):
            #     statuss[i]="BU email skipped"

            # Try to send the email
            else:
                try:
                    msg = MIMEMultipart('alternative')
                    msg['Subject'] = random.choice(subject_lines)
                    # "Be Honest - We'd Love to Hear Your Thoughts"
                    msg['From'] = from_email
                    msg['To'] = researcher_email

                    html = email_body.format(name=researcher_name.split()[0])

                    part1 = MIMEText(html, 'html')

                    msg.attach(part1)

                    mail.sendmail(from_email, researcher_email, msg.as_string())

                    statuss[i]="sent"
                    print(f"Sent to: {researcher_email}")
                # If cannot send, move on
                except Exception as e:
                    print(e)
                    statuss[i]="cannot be sent"
                    print("moving on")

            i += 1
            # time.sleep(1)

        # close server
        mail.quit()
        time.sleep(70)
        

    # update the status column in the csv file
    data["Status"] = statuss
    data.to_csv(filePath, index=False)

    print(f"{total} emails sent.")

    

# studyfind_sendEmails(r'C:\Users\alexa\ProgrammingProjects\studyfind\file-processor\to_email\0_2.csv', "anika.shah03@studyfind.org")

# SMTPServerDisconnected('please run connect() first')