from app.classes.RabbitHandler import RabbitQueueInformer
from app.classes.RabbitHandler import RabbitQueueConsumer

#получаем информацию по jobam
rab = RabbitQueueInformer()

# получаем список очередей
q =  rab.rest_queue_list()

# получаем список очередей Изображений
q_imgs = rab.check_img_queue()
print(q)
print(q_imgs)

# Делаем загрузку по первому элементу
qu = q_imgs[0]
worker = RabbitQueueConsumer(qu)

worker.start_consuming()