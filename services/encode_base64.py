from flask import request
import base64
from pathlib import Path
import os

def encode_pdf_to_base64(*args,**kwargs):
    pdf_file = request.files['file']
    max_size = 4 * 1024 * 1024

    # Save the uploaded file to a temporary directory
    tmp_dir = Path('/tmp')  # or any other temporary directory of your choice
    pdf_path = tmp_dir / pdf_file.filename
    pdf_file.save(str(pdf_path))

    # Read the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        pdf_data = pdf_file.read()

    # Encode the PDF data to Base64 string
    base64_data = base64.b64encode(pdf_data)

    # Check if the encoded data exceeds the maximum size
    if len(base64_data) > max_size:
        raise ValueError("Encoded data exceeds the maximum size of {} bytes".format(max_size))

    # Write the encoded data to a file in the same directory
    base64_path = tmp_dir / (pdf_path.stem + ".base64")
    with open(base64_path, 'wb') as base64_file:
        base64_file.write(base64_data)

    # Read the Base64-encoded data from the file
    with open(base64_path, 'rb') as base64_file:
        base64_data = base64_file.read()

    # Return the Base64-encoded data as a string
    return base64_data.decode('utf-8')


def check_to_base64(*args,**kwargs):
    
    # Retrieve JSON payload for base64
    data = request.json
    base64_string = data['BASE64']
    
    # Decode the base64 string into binary data
    binary_data = base64.b64decode(base64_string)

    # Check the size of the binary data in MB
    if len(binary_data) / (1024*1024) < 4:
        print("The base64 string is less than 4MB")
    else:
        print("The base64 string is greater than or equal to 4MB")




