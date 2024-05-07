import os
import shutil
import random
import zipfile
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def extract_and_split_images(zip_path, output_dir, train_ratio=0.8):
    train_dir = os.path.join(output_dir, 'Train')
    valid_dir = os.path.join(output_dir, 'Valid')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(valid_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
    
    print("Разархивация архива успешна!")

    for folder_name in os.listdir(output_dir):
        folder_path = os.path.join(output_dir, folder_name)

        print(f"Зашел в папку {folder_path}")
        if os.path.isdir(folder_path) and folder_path not in [train_dir, valid_dir]:
            images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
            random.shuffle(images)
            train_size = int(len(images) * train_ratio)

            for image in images[:train_size]:
                shutil.move(image, train_dir)
            print(f"Переместил изображения из папки {folder_path} в Train")
            for image in images[train_size:]:
                shutil.move(image, valid_dir)
            print(f"Переместил изображения из папки {folder_path} в Valid")

            #os.rmdir(folder_path)

zip_path = 'content/Africano/finger_1.zip'
output_dir = 'content/Africano/'
extract_and_split_images(zip_path, output_dir)
