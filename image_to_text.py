import pytesseract
from PIL import Image

notes = pytesseract.image_to_string(Image.open("abc.jpg"), lang="eng")
print(notes)
