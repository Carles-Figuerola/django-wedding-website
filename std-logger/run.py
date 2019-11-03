from flask import Flask
from flask import send_file
import json
app = Flask(__name__)

def send_notification(email, uuid):
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    from email.MIMEImage import MIMEImage
    
    # Define these once; use them twice!
    strFrom = 'Christine & Carles <christine.carles@figuerola.info>'
    strTo = strFrom

    # Create the root message and fill in the from, to, and subject headers
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = '[std-receipt] {} - {}'.format(email, uuid)
    msgRoot['From'] = strFrom
    msgRoot['To'] = strTo
    msgRoot.preamble = 'This is a multi-part message in MIME format.'

    # Encapsulate the plain and HTML versions of the message body in an
    # 'alternative' part, so message agents can decide which they want to display.
    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)

    msgText = MIMEText('')
    msgAlternative.attach(msgText)

    html_text = """
<html>
    <body>
        {} has read the Save The Date
    </body>
</html>
""".format(email)
    msgText = MIMEText(html_text, 'html')
    msgAlternative.attach(msgText)

    import smtplib
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp.login('christine.carles@figuerola.info', 'REDACTED')
    result = smtp.sendmail(strFrom, strTo, msgRoot.as_string())
    smtp.quit()
    print "email sent"
    print result


@app.route("/<string:email>/<string:uuid>")
def log(email, uuid):
    if '__' in email:
        email.replace('__','@')
        send_notification(email.replace('__','@'), uuid)
        return send_file('pixel.png', mimetype='image/png')
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
