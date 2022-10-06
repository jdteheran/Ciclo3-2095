import smtplib, ssl

def enviar_correo(destinatario, asunto, mensaje):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "curso2095@gmail.com"
    password = "tmqesbzofaduyzzs"
    message ="Subject:{} \n\n {}".format(asunto, mensaje)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, destinatario, message)