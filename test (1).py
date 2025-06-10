import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from rembg import remove

# Обратное отображение для сопоставления числовых меток с названиями стилей интерьера
label_mapping_inverse = {
    0:"Asian", 1:"Beach", 2:"Contemporary",
    3:"Craftsman", 4:"Farmhouse",5:"Industrial",
    6:"Mediterranean", 7:"Midcentury",8:"Modern",
    9:"Rustic",10:"Traditional", 11:"Transitional", 12:"Victorian"
}

# Загрузка модели
model = load_model('best_model_128.h5')

# Загрузка изображения
image = Image.open('D:\\dowland\\Diplodomik\\Helloword\\1\\processed_images_test\\2073486.jpg')
#image2= remove(image)
#image2.save('1.png')
resized_image = image.resize((128, 128))
#resized_image.save('1.jpg')
#resized_image = remove(resized_image)
# Преобразование изображения в массив numpy
image_array = np.array(resized_image)

# Нормализация изображения
image_array = image_array.astype("float32") / 255.

# Добавление измерения пакета
image_array = np.expand_dims(image_array, axis=0)

# Выполнение предсказания
prediction = model.predict(image_array)

# Получение отсортированного списка индексов классов по убыванию вероятности
sorted_indices = np.argsort(prediction[0])[::-1]
#print(sorted_indices)
# Вывод результатов с названиями стилей, номерами и процентами вероятностей
for i, idx in enumerate(sorted_indices):
    predicted_class_name = label_mapping_inverse[idx]
    prob = prediction[0][idx] * 100
    print(f"Rank {i + 1}: Class {idx} ({predicted_class_name}): {prob:.2f}%")

