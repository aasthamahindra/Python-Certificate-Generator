from numpy import imag
import pandas
from PIL import Image, ImageFont, ImageDraw
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

data = pandas.read_excel(r"C:\Users\pc xpertz\Desktop\Names.xlsx")
list = data["Name"].to_list()

for i in list:
    img = Image.open(r"C:\Users\pc xpertz\Documents\GitHub\Certificate_Generator\Sample_Certificate.png").convert('RGB')
    certificate = ImageDraw.Draw(img)
    location = (260,190)
    font = ImageFont.truetype("times.ttf", 20)
    certificate.text(location,i ,(0,0,0),font=font)
    img.save("Certificate_"+ i + ".pdf")
    

