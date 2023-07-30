from app.classes.RabbitHandler import RabbitQueueInformer
from app.classes.RabbitHandler import RabbitQueueConsumer

#получаем информацию по jobam
rab = RabbitQueueInformer()

# получаем список очередей
q =  rab.rest_queue_list()


worker = RabbitQueueConsumer('Images_to_download')
worker.start_consuming()