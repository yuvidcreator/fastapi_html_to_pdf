import os
from PIL import Image
from typing import Annotated
from fastapi import File
# from PyPDF2 import PdfReader, PdfWriter





# def compress_pdf(input_path):
#     output_path = "/compressed_pdfs"
#     '''# Compress PDF Using - PyPDF'''
#     reader = PdfReader(input_path)
#     writer = PdfWriter()

#     for page in reader.pages:
#         page.compress_content_streams()  # This is CPU intensive!
#         writer.add_page(page)

#     with open(output_path, "wb") as f:
#         writer.write(f)
    
#     return output_path


def print_file_size(file):
    File_Size = os.path.getsize(file)
    File_Size_MB = round(File_Size/1024/1024,2)
    print("Image File Size is " + str(File_Size_MB) + "MB" )



async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}