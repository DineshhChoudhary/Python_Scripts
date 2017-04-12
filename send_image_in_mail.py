import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

From="EMAIL@gmail.com"
To="EMAIL@gmail.com"
username="EMAIL@gmail.com"
password="PASSWORD"
ImageName='image.png'
def SendMail(ImageName):
    imag_data=open(ImageName,'rb').read()
    msg=MIMEMultipart()
    msg['Subject']='subject'
    msg['From']=From
    msg['To']=To

    text=MIMEText("test")
    msg.attach(text)
    image=MIMEImage(imag_data,name=os.path.basename(ImageName))
    msg.attach(image)

    s=smtplib.SMTP('smtp.gmail.com')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(username,password)
    s.sendmail(From,To,msg.as_string())
    s.quit()

SendMail(ImageName)
