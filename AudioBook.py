import pyttsx3
import PyPDF2

book = open("Class 102 Security System using webcam/AudioBook/storybook.pdf",'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(f" No of Pages in you Book are : {pages}")

speaker = pyttsx3.init()
rate = speaker.getProperty('rate')   
print(rate)

speaker.setProperty('rate', 125)
pgno = int(input("Page you want to read : "))
page = pdfReader.getPage(pgno+1)
text = page.extractText()

speaker.say(text)
speaker.runAndWait() 