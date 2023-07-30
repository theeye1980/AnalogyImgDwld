import time
import requests
from PIL import Image
from io import BytesIO
import os

class ImageDownloader:
    #Занимается загрузкой изображений
    def __init__(self):
        self.download_count = 0

    def download_image(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            with open(self.path, 'wb') as f:
                f.write(response.content)
            self.download_count += 1
            elapsed_time = time.time() - self.start_time
            print(f"Downloaded {self.download_count} images in {elapsed_time:.2f} seconds")
    @staticmethod
    def jpgTo224(url, path):
        # Check if the URL ends with ".jpg"
        if not url.lower().endswith(".jpg"):
            print("Invalid URL. The URL should point to a JPEG file.")
            return

        try:
            # Fetch the image from the URL
            response = requests.get(url)
            response.raise_for_status()

            # Load the image from the response content
            image = Image.open(BytesIO(response.content))

            # Calculate the new size while maintaining the aspect ratio
            width, height = image.size
            if width > height:
                new_width = 224
                new_height = int(height * (224.0 / width))
            else:
                new_height = 224
                new_width = int(width * (224.0 / height))

            # Create a new image with a white background and the new size
            new_image = Image.new("RGB", (224, 224), (255, 255, 255))

            # Calculate the coordinates to center the image
            x = (224 - new_width) // 2
            y = (224 - new_height) // 2

            # Resize and paste the original image onto the new image
            resized_image = image.resize((new_width, new_height))
            new_image.paste(resized_image, (x, y))


            # Save the new image as a JPEG file
            new_image.save(path, "JPEG")

            print("Image saved successfully.")

        except requests.exceptions.RequestException as e:
            print("Error fetching the image from the URL:", e)

        except IOError as e:
            print("Error processing the image:", e)

