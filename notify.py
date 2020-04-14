### EMAIL NOTIFICATION

def send(county, error):
    import smtplib

    gmail_user = 'czbiohubscraper@gmail.com'
    gmail_password = ''

    sent_from = gmail_user
    to = ['johnsimsemail@gmail.com']
    subject = 'Scrape Failed for ' + county + ''
    body = 'Hey, whats up?\n\n- You'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()
    except Exception as e:
        print(e)

#send()
