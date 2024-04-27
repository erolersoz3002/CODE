#hatırlatma file.pdf kısmını değiştirin
#modülleri içe alma
import PyPDF2
import pyttsx3

#Pdf dosyasını girin
path=open('file.pdf','rb')
#PdfFileReader objesini oluşturma
pdfReader=PyPDF2.PdfFileReader(path)
# Başlamak istediğiniz sayfayı giriniz
from_page = pdfReader.getPage(0)

# metini çıkarma
text = from_page.extractText()

# metni okuma
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()