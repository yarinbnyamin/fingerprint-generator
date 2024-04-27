import zipfile
import os
import shutil
from random import sample, shuffle
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

zip_path = 'content/Africano/finger_1.zip'

extract_to = 'content/Africano/'

os.makedirs(extract_to, exist_ok=True)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("Файлы успешно извлечены!")