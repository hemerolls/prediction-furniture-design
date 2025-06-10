import os
import gzip
from PIL import Image
import numpy as np
from keras.applications.mobilenet_v2 import preprocess_input

# Открываем файл с данными и считываем список путей к изображениям
with open('ffff_filtred_x_test.txt', 'r') as file:
    image_paths = file.readlines()

image_base_path = 'D:\\dowland\\Styles_Dataset'

num_parts = 5
total_images = len(image_paths)
images_per_part = total_images // num_parts
print(len(image_paths))
# Разделение списка на три части
part1 = image_paths[:images_per_part]
part2 = image_paths[images_per_part:2*images_per_part]
part3 = image_paths[2*images_per_part:3*images_per_part]
part4 = image_paths[3*images_per_part:4*images_per_part]
part5 = image_paths[4*images_per_part:]

# Создаем папку для сохранения измененных изображений
output_folder = 'processed_images_test'
os.makedirs(output_folder, exist_ok=True)

# Инициализируем список для хранения данных изображений и меток
processed_images = []

# Проходим по каждому пути к изображению, изменяем размер, сохраняем и добавляем в список
for idx, image_path in enumerate(image_paths):
    image_path = image_path.strip()  # Удаляем лишние пробелы и символы новой строки
    image_full_path = os.path.join(image_base_path, image_path)
    image = Image.open(image_full_path)
    #d = image_style[i]
    # Изменяем размер изображения (например, до 224x224)
    resized_image = image.resize((128, 128))  # Укажите требуемый размер
    #output_path = os.path.join(output_folder, f'image_{idx}.jpg')
    print(f'image_{idx}.jpg')
    #resized_image.save(output_path)
    
    # Преобразуем изображение в массив numpy
    processed_images.append(preprocess_input( (np.array(resized_image))))

# Архивируем список обработанных изображений и меток с использованием np.savez_compressed
with open('eq_valv2.npz.gz', 'wb') as f:
    np.savez_compressed(f, images=processed_images)


