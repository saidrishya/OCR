from wand.image import Image

pdf = Image(filename= "week1.pdf", resolution=300)
#the above cotains mul images
pdfImage = pdf.convert("jpeg")

i=1
for img in pdfImage.sequence:
    page = Image(image=img)
    page.save(filename= str(i)+".jpg")
    i = i+1
    
    

