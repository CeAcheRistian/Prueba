import smtplib #protocolo web, cada pagina usa uno, como http, ftp, telnet. Puede ser un canal seguro, si lo es, entocnes los datos son cifrados
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

def enviar_correo(correo_destinatario, cuerpo_correo, asunto_correo):
    remitente = "666monroy@gmail.com"
    destinatarios = []
    destinatarios.append(correo_destinatario)
    asunto = asunto_correo
    cuerpo = cuerpo_correo
    mensaje = MIMEMultipart()#Se instancia un objeto para mandar correos

    mensaje["From"] = remitente
    mensaje["To"] = ", ".join(destinatarios)
    mensaje["Subject"] = asunto
    
    mensaje.attach(MIMEText(cuerpo, 'plain'))

    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    sesion_smtp.starttls()
    sesion_smtp.login("666monroy@gmail.com", "tpdr iidk mnce zdlv")#correo,contraseña
    texto = mensaje.as_string()
    try:
        sesion_smtp.sendmail(remitente, destinatarios, texto)
    except:
        print('No se pudo enviar el correo')
    finally:
        sesion_smtp.quit()




def enviar_correo_img(correo_destinatario, asunto):
    remitente = '666monroy@gmail.com'
    destinatarios = []
    destinatarios.append(correo_destinatario)
    asunto = asunto
    cuerpo = "Envio automatico de imagenes"
    ruta_adjunto = 'nuevo.png'
    nombre_adjunto = 'nuevo.png'
    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    # Establecemos los atributos del mensaje
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    # Abrimos el archivo que vamos a adjuntar
    archivo_adjunto = open(ruta_adjunto, 'rb')
    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    mensaje.attach(adjunto_MIME)
    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # Ciframos la conexión
    sesion_smtp.starttls()
    # Iniciamos sesión en el servidor
    sesion_smtp.login('666monroy@gmail.com','tpdr iidk mnce zdlv')
    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()
    # Enviamos el mensaje
    try:
        sesion_smtp.sendmail(remitente, destinatarios, texto)
    except:
        print("No se Pudo enviar el Correo a:")
    # Cerramos la conexión
    sesion_smtp.quit()

enviar_correo("666monroy@gmail.com", "Hola", "Abreme")
enviar_correo_img("666monroy@gmail.com", "Holaaa")