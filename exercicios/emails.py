import os
import sys
import smtplib
from email.mime.text import MIMEText

arguments = sys.argv[1:]
if not arguments:
    print("Informe a base de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

with smtplib.SMTP(host="localhost", port=8025) as server:

    for line in open(filepath):
        name, email = line.split(",")
        text = (
            open(templatepath).read()
            % {
                "nome": name, 
                "produto": "caneta", 
                "texto": "Escrever muito bem",
                "link": "https://google.com",
                "quantidade": 1,
                "preco": 5.9,
            }
        )

        from_ = "myemail@gmail.com"
        to = ", ".join([email])

        message = MIMEText(text)
        message["Subject"] = "Compre mais"
        message["From"] = "myemail@domain.com"
        message["To"] = ", ".join([email])
        server.sendmail(from_, to, message.as_string())

   