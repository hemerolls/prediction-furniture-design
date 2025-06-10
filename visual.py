import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.python.keras.models import Model
import numpy as np
import matplotlib.pyplot as plt


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
#image = Image.open('D:\\dowland\\Diplodomik\\Helloword\\1\\processed_images_test\\image_375.jpg')
#resized_image = image.resize((128, 128))
# Преобразование изображения в массив numpy
#image_array = np.array(resized_image)

# Нормализация изображения
#image_array = image_array.astype("float32") / 255.0

# Добавление измерения пакета
#image_array = np.expand_dims(image_array, axis=0)

# Выполнение предсказания
#prediction = model.predict(image_array)
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.python.keras.models import Model
import numpy as np
import matplotlib.pyplot as plt


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
image = Image.open('D:\\dowland\\Diplodomik\\Helloword\\1\\processed_images_test\\image_375.jpg')
resized_image = image.resize((128, 128))
#Преобразование изображения в массив numpy
image_array = np.array(resized_image)

# Нормализация изображения
image_array = image_array.astype("float32") / 255.0

# Добавление измерения пакета
image_array = np.expand_dims(image_array, axis=0)

# Выполнение предсказания
prediction = model.predict(image_array)
print(prediction)
# Загрузка модели


# Получаем первый слой MobileNet
first_mobileNet_layer = model.layers[0]

# Создаем модель с входами и выходами
activation_model = Model(inputs=model.input, outputs=[layer.output for layer in first_mobileNet_layer.layers[:6]])
activation_model.summary()
