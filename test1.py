import os
import time
import pika
import re
from app.classes.ProjectSummary import ProjectSummary
from app.classes.ImageDownloader import ImageDownloader
from app.classes.DeepImageSearch_m import DeepImageSearch_m, Load_Data, Search_Setup
from app.classes.RabbitHandler import RabbitQueueInformer
from app.classes.RabbitHandler import RabbitQueueTaskSender
from app.classes.JsonPreparator import JsonPreparator
from app.classes.CategoryTranslite import CategoryTranslite


#получаем информацию по jobam
rab = RabbitQueueInformer()

# получаем список очередей
q =  rab.rest_queue_list()

print(q)

# получаем список очередей Изображений

