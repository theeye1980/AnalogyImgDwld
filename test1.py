from app.classes.RabbitHandler import RabbitQueueInformer
from app.classes.RabbitHandler import RabbitQueueConsumer
from app.classes.MinIOHandler import MinIOHandler

#получаем информацию по jobam
rab = RabbitQueueInformer()

# получаем список очередей
q =  rab.rest_queue_list()

worker = RabbitQueueConsumer('Images_to_download')
worker.start_consuming()

# mini = MinIOHandler()
# buckets = mini.list_buckets()
# ImgMiniFiles = mini.get_bucket_file_structure('models')



print("Усе")

