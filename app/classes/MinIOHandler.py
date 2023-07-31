import json
import os
import subprocess
from minio import Minio

class MinIOHandler:
    #Разбор и обработка данных из файла клиента
    #На входе url, далее сохраняем при инициализации класса, парсим и работаем с тем, что есть
    def __init__(self):
        with open('config.json') as f:
            config = json.load(f)
        self.minio_host = config['MINIO_SERVER']
        self.minio_ac = config['MINIO_AC']
        self.minio_sc = config['MINIO_SC']
        self.client = Minio(self.minio_host, access_key=self.minio_ac, secret_key=self.minio_sc)

    def list_buckets(self):
        return self.client.list_buckets()

    def get_bucket_file_structure(self, bucket_name):
        for item in self.client.list_objects(bucket_name, recursive=True):
            print(item.object_name)

    def upload_file(self, bucket_name, file_path, object_name=None):
        # if not object_name:
        #     object_name = os.path.basename(file_path)
        object_name = file_path
        self.client.fput_object(bucket_name, object_name, file_path)

    def download_file(self, bucket_name, object_name, file_path):
        self.client.fget_object(bucket_name, object_name, file_path)