# OCR Notes

OCR (Optical Character Recognition)

## I) Extract text from images
### Requirements
          1) Tesseract engine is an OCRengine + command line program + libtesseract (needs to be included in the path)
          2) a python package to bind to the engine (pytesseract or tesseract-ocr)
          3) an image processing libarary required, pillow or opencv, in opencv tesseract path has to be linked ; pillow doesn't require that

A simple command line statement would do the job.
```
tesseract image.extension filename.txt
opening the file --> type filename.txt (alternative to cat in unix)
```



## II) Extract text from pdf
### Requirements
           1) Wand is a python package
           2) Imagemagick is an engine again, that has to be included in the path and while installing c/c++ option should be 
     checked for wand to link with imagemagick
           3) Ghostscripts need to be installed for processing of pdf, jpg etc.

 
