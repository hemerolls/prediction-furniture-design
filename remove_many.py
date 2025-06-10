# Чтение данных из текстовых файлов
with open("x_megatrain.txt", "r") as f:
    x_train = f.readlines()

with open("y_train_val_styles.txt", "r") as f:
    y_styles = f.readlines()

# Удаление стилей Contemporary, Traditional и Transitional из y_styles и соответствующих изображений из x_train
styles_to_remove = ['Southwestern','Eclectic','Scandinavian','Tropical']

label_mapping = {
    "Asian": 0, "Beach": 1, "Contemporary": 2,
    "Craftsman": 3, "Farmhouse": 4,"Industrial": 5,
    "Mediterranean": 6, "Midcentury": 7,"Modern": 8,
    "Rustic": 9,"Traditional": 10, "Transitional": 11, "Victorian": 12
}
bath = "train_styles.txt"
bath2="x_train.txt"
labels = "filtred"+'_'+ bath
labels2= "filtred"+'_'+ bath2
# Фильтрация данных
filtered_x_train = []
filtered_y_styles = []
for x, y in zip(x_train, y_styles):
    style = y.strip()  # удаляем лишние пробелы и символы переноса строки
    if style not in styles_to_remove:
        filtered_x_train.append(x)
        filtered_y_styles.append(y)
        
# Сохранение отфильтрованных данных обратно в файлы
with open(labels2, "w") as f:
    f.writelines(filtered_x_train)

with open(labels, "w") as f:
    f.writelines(filtered_y_styles)

input_file_path = labels  # Путь к вашему исходному текстовому файлу
output_file_path = 'n_'+labels  # Путь к файлу, в который будет записан результат

# Чтение исходного файла
with open(input_file_path, "r") as f:
    content = f.read()

# Замена названий стилей на цифры
for style, label in label_mapping.items():
    content = content.replace(style, str(label))

# Запись результата в новый файл
with open(output_file_path, "w") as f:
    f.write(content)

print("Замена завершена. Результат записан в", output_file_path)
