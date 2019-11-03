#!/usr/bin/python

import sys

# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from optparse import OptionParser

parser = OptionParser()
parser.add_option('--email', '-e', dest='email', help='Destination email', default='carlesgf@gmail.com')
parser.add_option('--language', '-l', dest='language', help='language', default='eng')
parser.add_option('--debug', '-d', action='store_true', dest='debug', help='debug', default=False)
(options, args) = parser.parse_args()

strTo = options.email
lang = options.language
debug = options.debug

# Define these once; use them twice!
strFrom = 'Christine & Carles <christine.carles@figuerola.info>'

# Create the root message and fill in the from, to, and subject headers
import uuid
uuid = str(uuid.uuid4())
msgRoot = MIMEMultipart('related')
debug_message = ""
if debug:
    debug_message = " - test - " + uuid
if lang == 'cat':
    msgRoot['Subject'] = 'Carles '+unicode('\U00002764', 'unicode-escape')+' Christine - Esteu Convidats!' + debug_message
else:
    msgRoot['Subject'] = 'Carles '+unicode('\U00002764', 'unicode-escape')+' Christine - You Are Invited!' + debug_message
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

if lang == 'cat':
    msgText = MIMEText('Please join us for a celebration of our wedding in Chicago, May 18th 2019')
else:
    msgText = MIMEText('Esteu convidats a celebrar el nostre casament a Chicago, el 18 de Maig del 2019')
msgAlternative.attach(msgText)


#============== html content =============#
email_notification = strTo.replace('@','__')
import uuid
uuid = str(uuid.uuid4())

images_local = ""
images_local = images_local + """
<div class="std-div"><img class="std-img" alt="We would like you to: " title="We would like you to: " src="cid:save-the-date-header"></div>"""

images_local = images_local + """
<div border="0" class="std-div"><img class="std-img" alt="." title="." src="cid:save-the-date-arrow1"></div>
<div border="0" class="std-div"><img class="std-img" alt="." title="." src="cid:save-the-date-arrow2"></div>
<div border="0" class="std-div"><img class="std-img" alt="." title="." src="cid:save-the-date-arrow3"></div>
"""

images_local = images_local + """
<div class="std-div"><img class="std-img" alt="save the date: May 18 2019" title="save the date: May 18 2019" src="cid:save-the-date-main"></div>
"""

if lang == 'cat':
    images_local = images_local + """
<div class="std-div"><a href="https://docs.google.com/forms/d/e/1FAIpQLScGn954W1fBWWhPTH-3OoZL9fBP9WvBoQ_Uvz6MbuP8FlUM2A/viewform"><img class="std-img" alt="Cliqueu per confirmar assist%C3%A8ncia" title="Cliqueu per confirmar assist%C3%A8ncia" src="cid:save-the-date-rsvp"></a></div>
"""
else:
    images_local = images_local + """
<div class="std-div"><a href="https://docs.google.com/forms/d/e/1FAIpQLSfTC4ZpbLOD1O9_mtR6p1p2vn1mFij034OfjLf64yqUq2mI_Q/viewform"><img class="std-img" alt="Click here to RSVP" title="Click here to RSVP" src="cid:save-the-date-rsvp"></a></div>
"""

images_local = images_local + """
<div class="std-div"><img class="std-img" alt="for our Wedding in Chicago" title="for our Wedding in Chicago" src="cid:save-the-date-footer"></div>
"""

if lang == 'cat':
    images_local = images_local + """
<div class="std-div"><a href="https://carlesichristine.figuerola.info/barcelona"><img class="std-img" alt="Visit our website: https://carlesichristine.figuerola.info/barcelona" title="Visit our website: https://carlesandchristine.figuerola.info/barcelona" src="cid:save-the-date-website"></a></div>
"""
else:
    images_local = images_local + """
<div class="std-div"><a href="https://carlesandchristine.figuerola.info/barcelona"><img class="std-img" alt="Visit our website: https://carlesandchristine.figuerola.info/barcelona" title="Visit our website: https://carlesandchristine.figuerola.info/barcelona" src="cid:save-the-date-website"></a></div>
"""



# We reference the image in the IMG SRC attribute by the ID we give it below
html_text = """
<html>
        <head>
                <style>
                img + div { display:none; }
                .std-div {
                        border: 0;
                        margin: 0;
                        text-align: center;
                }
                .std-img {
                        border: 0;
                        margin: 0;
                        text-align: center;
                        width: 768px;
                        display: block;
                        margin: auto;
                }
                @media(max-width:768px) {
                        .std-div {
                                border: 0;
                                margin: 0;
                                text-align: center;
                        }
                        .std-img {
                                border: 0;
                                margin: 0;
                                text-align: center;
                                width: 100%;
                                display: block;
                                margin: auto;
                        }
                        }
                </style>
        </head>
        <body>"""+images_local+ """
            <div><img src="http://carlesandchristine.figuerola.info:8080/"""+email_notification+"/"+uuid+""""></div>
        </body>
</html>
"""

msgText = MIMEText(html_text, 'html', _charset='iso-8859-1')
msgAlternative.attach(msgText)

format = 'jpg'
list = [
        'save-the-date-header.{}'.format(format),
        'save-the-date-main-{}.{}'.format(lang, format),
        'save-the-date-rsvp-{}.{}'.format(lang, format),
        'save-the-date-footer.{}'.format(format),
        'save-the-date-website-{}.{}'.format(lang, format)
        ]
for filename in list:
    with open(filename, 'rb') as fp:
        msgImage = MIMEImage(fp.read())
        msgImage.add_header('Content-ID', '<' + '-'.join(filename.split('.')[0].split('-')[0:4]) + '>')
        msgRoot.attach(msgImage)


# Send the email (this example assumes SMTP authentication is required)
import smtplib
msgRoot.add_header('List-Unsubscribe', '<mailto:unsubscribe@figuerola.info>')
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login('christine.carles@figuerola.info', 'REDACTED')

response = smtp.sendmail(strFrom, strTo, msgRoot.as_string())
print lang.upper() + ": sent to {}, result: ".format(strTo) + str(response)
#print response
smtp.quit()
