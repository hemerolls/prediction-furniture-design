import os
import gzip
from PIL import Image
import numpy as np

# Открываем файл с данными меток и считываем список меток
with open('y_test_norm.txt', 'r') as file:
    labels = file.readlines()
    
num_parts = 4
total_images = len(labels)
images_per_part = total_images // num_parts

# Разделение списка меток на три части
labels_part1 = labels[:images_per_part]
labels_part2 = labels[images_per_part:2*images_per_part]
labels_part3 = labels[2*images_per_part:3*images_per_part]
labels_part4 = labels[3*images_per_part:]



output_folder = 'processed_labels'

# Создаем папку для сохранения файлов меток, если она не существует
os.makedirs(output_folder, exist_ok=True)

# Сохраняем каждую часть меток в отдельный файл
with open(os.path.join(output_folder, 'y_test_norm1.txt'), 'w') as file:
    file.writelines(labels_part1)

with open(os.path.join(output_folder, 'y_test_norm2.txt'), 'w') as file:
    file.writelines(labels_part2)

with open(os.path.join(output_folder, 'y_test_norm3.txt'), 'w') as file:
    file.writelines(labels_part3)
    
with open(os.path.join(output_folder, 'y_test_norm4.txt'), 'w') as file:
    file.writelines(labels_part4)
