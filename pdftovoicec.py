#Making Audio Book From Any PDF Using Python 
#pip install pyttsx3
#pip install PyPDF2'''
import pyttsx3
import PyPDF2
pdf = input("enter the pdf name : ")
pdf_book = open(pdf,'rb')
reading_pdf = PyPDF2.PdfFileReader(pdf_book)
#reading_pdf=reading_pdf1.strip()
pdf_pages = reading_pdf.numPages #pages start from 0 index

#for speaker
pdf_speaker = pyttsx3.init()
page_number = int(input("\n enter a page number to start reading (format: Actual page number - 1) : "))
choose_page = reading_pdf.getPage(page_number) #pages start works on  index (index allways start with 0)(page number - 1)

#only to choose text and skip images(extracting text)
pdf_text = choose_page.extractText()
pdf_speaker.say(pdf_text)
pdf_speaker.runAndWait()







