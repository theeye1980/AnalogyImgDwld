import time
import requests

class ImageTransformer:
    #Занимается преобразованием изображений
    def __init__(self, url_list):
        self.url_list = url_list
        self.download_count = 0
        self.start_time = time.time()

    def download_image(self, url , IdCliend, IdProject, Category):
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"Img/{IdCliend}/{IdProject}/{Category}/{self.download_count}.jpg", 'wb') as f:
                f.write(response.content)
            self.download_count += 1
            elapsed_time = time.time() - self.start_time
            print(f"Downloaded {self.download_count} images in {elapsed_time:.2f} seconds")


