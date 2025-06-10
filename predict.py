import csv
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from rembg import remove

# Обратное отображение для сопоставления числовых меток с названиями стилей интерьера
label_mapping_inverse = {
    0: "Asian", 1: "Beach", 2: "Contemporary",
    3: "Craftsman", 4: "Farmhouse", 5: "Industrial",
    6: "Mediterranean", 7: "Midcentury", 8: "Modern",
    9: "Rustic", 10: "Traditional", 11: "Transitional", 12: "Victorian"
}

# Загрузка модели
model = load_model('best_model_128.h5')

def process_image(image_path):
    # Загрузка изображения
    image = Image.open(image_path)
    
    # Удаление фона (опционально)
    #image = remove(image)
    
    # Изменение размера изображения
    resized_image = image.resize((128, 128))
    
    # Преобразование изображения в массив numpy
    image_array = np.array(resized_image)
    
    # Нормализация изображения
    image_array = image_array.astype("float32") / 255.0
    
    # Добавление измерения пакета
    image_array = np.expand_dims(image_array, axis=0)
    
    return image_array

def predict_styles(image_array):
    # Выполнение предсказания
    prediction = model.predict(image_array)
    
    # Получение отсортированного списка индексов классов по убыванию вероятности
    sorted_indices = np.argsort(prediction[0])[::-1]
    
    # Получение трех лучших стилей
    top_styles = [label_mapping_inverse[idx] for idx in sorted_indices[:3]]
    
    return top_styles

# Открываем CSV файл для чтения
with open("updated_dressers.csv", mode="r", newline="") as infile, open("updated_dressers_2.csv", mode="w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Чтение заголовка
    headers = next(reader)
    # Добавление новых заголовков для стилей
    headers.extend(['top1_style', 'top2_style', 'top3_style'])
    writer.writerow(headers)
    
    for row in reader:
        image_url = row[9]  # Предполагается, что ссылка на изображение находится в 10-й колонке (индекс 9)
        image_id = row[0]   # Предполагается, что ID изображения находится в 1-й колонке (индекс 0)
        if(image_url=='image_small'):
            continue
        # Путь к загруженному изображению
        image_path = f"dressers/{image_id}.jpg"
        
        try:
            # Обработка изображения
            image_array = process_image(image_path)
            
            # Предсказание стилей
            top_styles = predict_styles(image_array)
            
            # Добавление предсказанных стилей в строку
            row.extend(top_styles)
        except Exception as e:
            print(f"Ошибка при обработке изображения {image_id}: {e}")
            row.extend(['N/A', 'N/A', 'N/A'])
        
        # Запись обновленной строки в новый CSV файл
        writer.writerow(row)

print("Обновление CSV файла завершено.")
