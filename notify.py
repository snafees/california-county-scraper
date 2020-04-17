### EMAIL NOTIFICATION

def send(county, error):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "czbiohubscraper@gmail.com"
    password = ""
    toaddr = ['johnsimsemail@gmail.com']

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = ", ".join(toaddr)
    msg['Subject'] = "Scraping Error Notification"

    body = """\
    <html>
      <head></head>
      <body>
    <p>DO NOT REPLY TO THIS EMAIL<br>
    <br>
    The scraper for <b>""" + county + """</b> failed with the error message<br>
    <br>
    <b><i>""" + str(error) + """</i></b> <br>
    <br>
    Please dubug the script locally and update the corrected file in the server asap.
    <br>
        </p>
      </body>
    </html>
    """

    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.close()

#send('Sonoma', 'This is an error')
