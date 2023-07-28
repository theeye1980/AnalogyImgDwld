import json
import re

class MinIOHandler:
    #Разбор и обработка данных из файла клиента
    #На входе url, далее сохраняем при инициализации класса, парсим и работаем с тем, что есть
    def __init__(self):
        with open('config.json') as f:
            config = json.load(f)

        self.db_cursor = self.db_connection.cursor()
