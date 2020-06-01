import os
os.system("cls||clear")
print("\n")
# ----------------------------------------------------------------------


# endereço para permitir que usar o gmail com programas não seguros como esse
# https://myaccount.google.com/u/3/lesssecureapps?pageId=none

import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

VIRGULA = ', '

sender = 'univelaluno@gmail.com'       # usuário do servidor de e-mail
gmail_password = 'Aluno123456'         # senha do e-mail utilizado
recipients = ['univelaluno@gmail.com'] # lista de e-mails de destinatários
text = "Mensagem de e-mail teste."     # o que vai no corpo do e-mail

# texto em HTML que deseja enviar por e-mail
html = """
<html>

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">

   <title>Tutsplus Email Newsletter</title>
   <style type="text/css">
    a {color: #d80a3e;}
  body, #header h1, #header h2, p {margin: 0; padding: 0;}
  #main {border: 1px solid #cfcece;}
  img {display: block;}
  #top-message p, #bottom p {color: #3f4042; font-size: 12px; font-family: Arial, Helvetica, sans-serif; }
  #header h1 {color: #ffffff !important; font-family: "Lucida Grande", sans-serif; font-size: 24px; margin-bottom: 0!important; padding-bottom: 0; }
  #header p {color: #ffffff !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; font-size: 12px;  }
  h5 {margin: 0 0 0.8em 0;}
    h5 {font-size: 18px; color: #444444 !important; font-family: Arial, Helvetica, sans-serif; }
  p {font-size: 12px; color: #444444 !important; font-family: "Lucida Grande", "Lucida Sans", "Lucida Sans Unicode", sans-serif; line-height: 1.5;}
   </style>
</head>

<body>


<table width="100%" cellpadding="0" cellspacing="0" bgcolor="e4e4e4"><tr><td>
<table id="top-message" cellpadding="20" cellspacing="0" width="600" align="center">
    <tr>
      <td align="center">
        <p><a href="#">Veja no Navegador</a></p>
      </td>
    </tr>
  </table>

<table id="main" width="600" align="center" cellpadding="0" cellspacing="15" bgcolor="ffffff">
    <tr>
      <td>
        <table id="header" cellpadding="10" cellspacing="0" align="center" bgcolor="8fb3e9">
          <tr>
            <td width="570" align="center"  bgcolor="#d80a3e"><h1>Univel Spam</h1></td>
          </tr>
          <tr>
            <td width="570" align="right" bgcolor="#d80a3e"><p>Maio 2020</p></td>
          </tr>
        </table>
      </td>
    </tr>

    <tr>
      <td>
        <table id="content-3" cellpadding="0" cellspacing="0" align="center">
          <tr>
              <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
              <img src="https://www.univel.br/sites/default/files/styles/thumb_370_444/public/home/destaque/whatsapp_image_2020-03-16_at_20.39.37.jpeg_0.jpg?itok=1q4LXzuH" width="250" height="150"  />
            </td>
              <td width="15"></td>
            <td width="250" valign="top" bgcolor="d0d0d0" style="padding:5px;">
                <img src="https://www.univel.br/sites/default/files/styles/thumb_370_444/public/home/destaque/e0cc6d9d-164e-4550-befe-146da37e9a5c_0.jpg?itok=Sa0GusUI" width ="250" height="150" />
            </td>
          </tr>
        </table>
      </td>
    </tr>
    <tr>
      <td>
        <table id="content-4" cellpadding="0" cellspacing="0" align="center">
          <tr>
            <td width="200" valign="top">
              <h5>Titulo 1</h5>
              <p>Algum texto aqui 1</p>
            </td>
            <td width="15"></td>
            <td width="200" valign="top">
              <h5>Titulo 2</h5>
              <p>Alguma coisa aqui ...</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>


  </table>
  <table id="bottom" cellpadding="20" cellspacing="0" width="600" align="center">
    <tr>
      <td align="center">
        <p>Desenvolvido para uma melhor experiência web & mobile</p>
        <p><a href="#">Unsubscribe</a> | <a href="#">Tweet</a> | <a href="#">View in Browser</a></p>
      </td>
    </tr>
  </table><!-- top message -->
</td></tr></table><!-- wrapper -->

</body>
</html>
"""


# criar um objeto para anexar as partes do e-mail e permitir que seja enviado
obj_mail = MIMEMultipart()
obj_mail['Subject'] = "Assunto do e-mail"  # assunto do e-mail
obj_mail['To'] = VIRGULA.join(recipients)  # adiciona os e-mails dos destinatários separados por vírgula
obj_mail['From'] = sender				   # coloca o e-mail do remetente



# adicionar as partes do email, tipo: html, texto, etc.
obj_mail.attach(MIMEText(text,'plain'))
obj_mail.attach(MIMEText(html,'html'))
obj_mail.preamble = 'O usuário não verá essa mensagem.\n'

# lista de anexos
anexos = ['/home/tampelini/Imagens/eq.jpg']
#anexos = ['C:\\Users\\tampe\\Desktop\\email\\01.jpg', 'C:\\Users\\tampe\\Desktop\\email\\02.jpg']


# anexar arquivos no e-mail
for nome_arq in anexos:
	try:
		# abrir os arquivos
		with open(nome_arq, 'rb') as fp:
			msg = MIMEBase('application', 'octet-stream')
			msg.set_payload(fp.read())

		# servidores de email exigem conversão para base64
		encoders.encode_base64(msg)

		# habilitei o anexo dos arquivos passando o caminho
		msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(nome_arq))


		# coloca o anexo preparado em nosso obj
		obj_mail.attach(msg)


	except:
		print("Não foi possível abrir os arquivos.")
		raise


# converte o objeto para string
composed = obj_mail.as_string()

# enviar o email que preparamos por meio do obj_mail
try:
	with smtplib.SMTP('smtp.gmail.com', 587) as s:
		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(sender, gmail_password)
		s.sendmail(sender, recipients, composed.encode("utf8"))
		s.close()
except:
	print("Não foi possível enviar o e-mail.")
	raise
else:
	print("Email enviado.")