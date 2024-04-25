import zipfile
import os
import shutil
from random import sample
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

zip_path = 'content/Africano/Real.zip'

extract_to = 'content/Africano/Real'

os.makedirs(extract_to, exist_ok=True)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("Файлы успешно извлечены!")

# Пути к директориям
source_directory = 'content/Africano/Real'
target_directory = 'content/Africano/Valid'

# Создание целевой папки, если она не существует
os.makedirs(target_directory, exist_ok=True)

# Получаем список всех изображений в исходной папке
images = [file for file in os.listdir(source_directory) if file.endswith(('BMP', 'jpg', 'jpeg'))]

# Выбираем 20% изображений для перемещения
images_to_move = sample(images, k=int(0.2 * len(images)))

# Перемещаем выбранные изображения
for image in images_to_move:
    shutil.move(os.path.join(source_directory, image), os.path.join(target_directory, image))

print("Изображения успешно перемещены!")
