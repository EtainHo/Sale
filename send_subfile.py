import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "etainltoc@gmail.com"
toaddr = "etain.stho@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Found it!"

import subfile
body = subfile.func()
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "acommons")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
