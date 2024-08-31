from google.cloud import vision

from receipt_parsers import tedi_receipt_parser

def run_quickstart() -> vision.EntityAnnotation:
  client = vision.ImageAnnotatorClient()
  
  with open('./assets/receipt-001.jpeg', "rb") as image_file:
    content = image_file.read();
  
  image = vision.Image(content=content)
  
  response = client.text_detection(image=image)
  texts = response.text_annotations
  
  print(tedi_receipt_parser.parse_receipt_from_tedi(texts))

  if response.error.message:
      raise Exception(
          "{}\nFor more info on error messages, check: "
          "https://cloud.google.com/apis/design/errors".format(response.error.message)
      )
    
  return texts

run_quickstart()