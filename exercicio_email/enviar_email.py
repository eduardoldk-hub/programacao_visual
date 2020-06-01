# limpar o console -----------------------------------------------------
#import os
#os.system('cls||clear')
#print('\n')
# ----------------------------------------------------------------------
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
#Parte relacionada ao arquivo---------
arq_msg = open("mensagem.txt", "r")
arq_emails = open("email.txt", "r")

arquivo_mensagem = arq_msg.read()
arquivo_emails = arq_emails.readlines()


VIRGULA = ", "


for e in range(len(arquivo_emails)):
	arquivo_emails[e]=arquivo_emails[e].rstrip()	
    
emails = arquivo_emails
texto_do_email  = arquivo_mensagem



#Parte relacionada ao email
remetente = 'univelaluno@gmail.com'
senha_gmail_remetente = "Aluno123456"
destinatario = emails
mensagem = texto_do_email

objeto_email = MIMEMultipart()
objeto_email["Subject"] = "Assunto tratado no email"
objeto_email["To"] = VIRGULA.join(destinatario)
objeto_email["From"] = remetente

# converte o objeto para string
composed = objeto_email.as_string()

# enviar o email que preparamos por meio do obj_mail
try:
	with smtplib.SMTP('smtp.gmail.com', 587) as s:
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(remetente, senha_gmail_remetente)
		s.sendmail(remetente, destinatario, composed.encode("utf8"))
		s.close()
except:
	print("Não foi possível enviar o e-mail.")
	raise
else:
	print("Email enviado.")