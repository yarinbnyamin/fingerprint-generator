import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def update_path():
    current_path = os.getcwd()
    file_path = os.path.join(current_path, 'configs/paths_config.py')
    with open(file_path, 'r') as file:
        config_content = file.read()
    train_path = os.path.join(current_path, "content/Africano/Train")
    valid_path = os.path.join(current_path, "content/Africano/Valid")

    new_config_content = config_content.replace("'nist_sd14_gt_train': '',", f"'nist_sd14_gt_train': '{train_path}',")
    new_config_content = new_config_content.replace("'nist_sd14_gt_test': '',", f"'nist_sd14_gt_test': '{valid_path}',")

    # Записываем изменения обратно в файл
    with open(file_path, 'w') as file:
        file.write(new_config_content)

def main():
    update_path()

    print("Пути успешно обновлены в файле configs/paths_config.py.")

if __name__ == "__main__":
    main()
