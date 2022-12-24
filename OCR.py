from pdf2image import convert_from_path
import os
import pytesseract
#import library for Image.open
from PIL import Image
def convert_pdf_image(pdf_path, dpi=200):
    # convert pdf to image
    # pdf_path: path of pdf file
    # dpi: resolution of image
    # return: list of image path
    pages = convert_from_path(pdf_path, dpi)
    image_path = []
    for page in pages:
        filename = "TestNotePages/"+str(page)+'.png'
        image_path.append(filename)
        page.save(filename, 'PNG')
    return image_path

def ocr(image_path):
    # ocr
    # image_path: path of image file
    # return: string of text
    return pytesseract.image_to_string(Image.open(image_path))

def ocr_pdf(pdf_path, dpi=200):
    # ocr pdf
    # pdf_path: path of pdf file
    # dpi: resolution of image
    # return: string of text
    image_path = convert_pdf_image(pdf_path, dpi)
    text = ''
    for path in image_path:
        text += ocr(path)
    return text

def main():
    #print all files within TestNotes folder 
    for file in os.listdir("TestNotes"):
        text = ocr_pdf("TestNotes/" + file)
        #print the text of each file
        print("Filename is " + file)
        print(text)

#run main function
if __name__ == '__main__':
    main()
