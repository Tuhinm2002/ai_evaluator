import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext('image.jpeg')

for bbox,text,prob in result:
    print(text)