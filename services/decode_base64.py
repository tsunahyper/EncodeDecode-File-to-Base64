from flask import request
import base64

def decode_base64_to_pdf(*args,**kwargs):
    
    data = request.json
    base64_string = data['file']

    # Decode the Base64 string
    decoded_data = base64.b64decode(base64_string)

    # Save the decoded data as a PDF file
    with open("decoded.pdf", "wb") as f:
        f.write(decoded_data)
    
    # Read the decoded data from the file
    with open("decoded.pdf", "rb") as f:
        pdf_data = f.read()
      
    return (pdf_data)




