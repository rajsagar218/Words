# Handwritten character recognition

- Code uses pyTessaract OCR library
- Works with Python 2.x or 3.x
- Stores OCR text in `output.txt` file


## Setup
- Install `tessaract` library [from official source](https://github.com/tesseract-ocr/tessdoc/blob/master/Home.md) 
- Install `pytesseract` [package from pip](https://pypi.org/project/pytesseract/)
```
pip install pytesseract==0.3.3
```

## Usage
- Call `main.py` with image location as argument. For instance
```
python main.py sample/test1.jpeg
```

## More info
- Google OCR API: https://cloud.google.com/vision/docs/ocr
- Google [handwritten text extraction](https://cloud.google.com/vision/docs/handwriting#try_it); can even try for free
- Tutorial: https://www.pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/