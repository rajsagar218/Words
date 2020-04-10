import Image
import pytesseract
import sys

# If you don't have tesseract executable in your PATH, include the following:
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract' (for windows)
# Example tesseract_cmd = /usr/bin/tesseract (for linux)
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'

if __name__ == "__main__":    
    if len(sys.argv) == 1:
        print('No input image file specified')
    else:
        text = pytesseract.image_to_string(Image.open(sys.argv[1]))
        text = text.encode('utf-8')
        with open('output.txt','w') as f:
            f.write(text)
