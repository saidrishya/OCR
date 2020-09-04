import pytesseract
import io
from wand.image import Image as wa
from PIL import Image


pdf = wa(filename="week1.pdf", resolution=300)
pdfImage = pdf.convert('jpeg')

imgBlobs = []

for img in pdfImage.sequence:
    page = wa(image= img)
    imgBlobs.append(page.make_blob('jpeg'))


extracted_text = []

for imgBlob in imgBlobs:
    im = Image.open(io.BytesIO(imgBlob))
    text = pytesseract.image_to_string(im, lang='eng')
    extracted_text.append(text)


print(extracted_text[0])
