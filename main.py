import pyttsx3
import PyPDF2

book = open('Python.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

#voices = speaker.getProperty('voices')
#for voice in voices:
   # to get the info. about various voices in our PC
#    print("Voice:")
#    print("ID: %s" % voice.id)
#    print("Name: %s" % voice.name)
#    print("Age: %s" % voice.age)
#    print("Gender: %s" % voice.gender)
#    print("Languages Known: %s" % voice.languages)

speaker = pyttsx3.init()
voice_id = "com.apple.speech.synthesis.voice.Alex"
speaker.setProperty('voice', voice_id)

for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

