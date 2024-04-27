import os
import shutil
from random import sample, shuffle
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def move_files_by_ratio(source_folder, dest_folder_80, dest_folder_20):

    if not os.path.exists(dest_folder_80):
        os.makedirs(dest_folder_80)
    if not os.path.exists(dest_folder_20):
        os.makedirs(dest_folder_20)
    
    for root, dirs, files in os.walk(source_folder):
        if files:
            files = [f for f in files if os.path.isfile(os.path.join(root, f))]
            distribute_files(files, root, dest_folder_80, dest_folder_20)

def distribute_files(files, current_folder, dest_folder_80, dest_folder_20):
    shuffle(files)
    total_files = len(files)
    split_index = int(0.8 * total_files) 

    for i, file in enumerate(files):
        original_file_path = os.path.join(current_folder, file)
        if i < split_index:
            shutil.move(original_file_path, os.path.join(dest_folder_80, os.path.basename(file)))
        else:
            shutil.move(original_file_path, os.path.join(dest_folder_20, os.path.basename(file)))


current_path = os.getcwd()
source_folder = os.path.join(current_path, 'content/Africano/finger_1')  
dest_folder_80 = os.path.join(current_path, 'content/Africano/Train')
dest_folder_20 = os.path.join(current_path, 'content/Africano/Valid') 

move_files_by_ratio(source_folder, dest_folder_80, dest_folder_20)
