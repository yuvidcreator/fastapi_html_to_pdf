import os
from PIL import Image
from typing import Annotated
from fastapi import File



def compress_image_pillow(input_path, output_path, quality=85):
    '''# Compress Using - Pillow'''
    with Image.open(input_path) as img:
        # img.save(output_path, "JPEG", quality=quality) # For JPG Images
        img.save(output_path, "PNG", optimize=True) # For PNG Images
    return img



def print_file_size(file):
    File_Size = os.path.getsize(file)
    File_Size_MB = round(File_Size/1024/1024,2)
    print("Image File Size is " + str(File_Size_MB) + "MB" )



async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}