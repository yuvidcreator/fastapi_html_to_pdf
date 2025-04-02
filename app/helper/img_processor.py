import os
from PIL import Image


# Defining a Python user-defined exception
class Error(Exception):
    """Base class for other exceptions"""
    pass



async def old_way_img_convert(image_file, which_format, quality):
    ''' # Image Compression Only'''
    output_image_path = "converted_images/"
    os.makedirs(output_image_path, exist_ok=True)

    Image.MAX_IMAGE_PIXELS = 933120000

    with Image.open(image_file) as img_obj:
        # Spliting the image path (to avoid the .jpg or .png being part of the image name):
        image_name = output_image_path.split('.')[0]
        image_ext = output_image_path.split('.')[1]
        # OR
        if image_ext != which_format:
            img_obj.save(f"{output_image_path}{image_name}.{which_format}", f"{which_format}", optimize=True, quality=quality if quality else 85)
        else:
            # img_obj.save(output_image_path, "JPEG", quality=quality) # For JPG Images
            img_obj.save(output_image_path, "PNG", optimize=True, quality=quality if quality else 85) # For PNG Images
    return img_obj


class ConvertImageToWebp:
    output_image_path = "converted_images/"
    os.makedirs(output_image_path, exist_ok=True)

    @classmethod
    def convert_to_webp(cls, input_image_path):
        '''# Convert Using - Pillow'''
        Image.MAX_IMAGE_PIXELS = 933120000
        with Image.open(input_image_path) as img:
            img.convert("RGB") # "L", "RGB", "CMYK"
            # Spliting the image path (to avoid the .jpg or .png being part of the image name):
            image_path = input_image_path.split('.')[0]
            image_name = image_path.split('/')[1]
            image_ext = input_image_path.split('.')[1]
            print(f"The image name is --> {image_name} and format is --> .{image_ext}")

            # Saving the images based upon their specific type:
            if image_ext == 'webp':
                return img
            elif image_ext == 'jpg' or image_ext == 'jpeg' or image_ext == 'png':
                img.save(f"{ConvertImageToWebp.output_image_path}{image_name}.webp", 'webp')
            else:
                # Raising an error if we didn't get a jpeg or png file type!
                raise Error
        return img
    
    @classmethod
    def bulk_convert_to_webp(cls, bulk_image_dir) -> list:
        '''# Bulk Convert Using - Pillow'''

        # We list all of the files and folders using os.listdir()
        image_files = os.listdir(bulk_image_dir) 
        # print(f"These are all of the files in our current working directory: {files}")

        # filter all of the images in our current working directory
        images = [image_file for image_file in image_files if image_file.endswith(('jpg', 'png', 'jpeg'))]
        converted_images = []

        for image in images:
            new_image = cls.convert_to_webp(image)
            converted_images.append(new_image)
        
        return converted_images
    
    @staticmethod
    def compress_image_pillow(input_path, output_path, quality=85):
        '''# Single Image Compress Using - Pillow'''
        Image.MAX_IMAGE_PIXELS = 933120000

        with Image.open(input_path) as img:
            # img.save(output_path, "JPEG", quality=quality) # For JPG Images
            img.save(output_path, "PNG", optimize=True) # For PNG Images
        return img



img_obj = ConvertImageToWebp()

img = img_obj.convert_to_webp(input_image_path="static/Group_33918.png")