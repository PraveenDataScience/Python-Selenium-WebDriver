import pyttsx3,PyPDF2
pdfReader=PyPDF2.PdfFileReader(open("File_1.pdf",'rb'))
audio=pyttsx3.init()
for page_num in range(pdfReader.numPages):
    text=pdfReader.getPage(page_num).extractText()
    cleanText=text.strip().replace('\n',' ')
    print(cleanText)
    audio.say(cleanText)
    audio.save_to_file(cleanText,'File_1.mp3')
    audio.runAndWait()
audio.stop()
