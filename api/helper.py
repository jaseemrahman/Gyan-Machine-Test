from PIL import Image
import os
 
#Function to Convert webp
class ImageConverter:
    @staticmethod
    def convert_to_webp(image_path):
        img = Image.open(image_path)
        file_extension = os.path.splitext(image_path)[1].lower()
        print("file1",file_extension)
        media_dir = 'media/test'  
        output_path = f"{image_path.replace(file_extension, '.webp')}"
        output_path = os.path.join(media_dir, output_path)
        img.save(output_path, 'WEBP')
        return output_path
