
class ProjectSummary:
    #Разбор и обработка данных проекта
    #На входе ID клиента, URL проекта, ID проекта и массив категорий для создания индекса
    def __init__(self, ClientId = 45, IdProject = 2, encoding='utf-8'):
        self.ClientId = ClientId
        self.IdProject = IdProject
        self.XMLUrl = "https://fandeco.ru/media/xml/for_trendsveta.xml"
        self.CategoriesToDwld = ["Подсветки для зеркал", "Трековые светильники"]
        self.BaseImgPath = f"Img/{self.ClientId}/{self.IdProject}"
        self.PretrainedModel = 'vgg19'
        self.BaseIndexPath = f"Indexes/{self.ClientId}/{self.IdProject}"

