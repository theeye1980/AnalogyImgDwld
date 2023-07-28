import json
class JsonPreparator:
    #Разбор и обработка данных из файла клиента
    #На входе url, далее сохраняем при инициализации класса, парсим и работаем с тем, что есть
    def __init__(self):
        self.json = []

    def Pack_ImgURL_to_json(self, path, pictureURL):
        data = {
            "path": path,
            "pictureURL": pictureURL
        }
        json_data = json.dumps(data)
        return json_data
