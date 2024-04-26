import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def update_paths_in_config(file_path, train_path, test_path):
    with open(file_path, 'r') as file:
        config_content = file.read()

    new_config_content = config_content.replace("'nist_sd14_gt_train': '',", f"'nist_sd14_gt_train': '{train_path}',")
    new_config_content = new_config_content.replace("'nist_sd14_gt_test': '',", f"'nist_sd14_gt_test': '{test_path}',")

    with open(file_path, 'w') as file:
        file.write(new_config_content)

def main():
    file_path = input("Введите путь к файлу: ")

    if not os.path.exists(file_path):
        print("Файл не найден.")
        return

    train_path = input("Введите новый путь для Train: ")
    test_path = input("Введите новый путь для Valid: ")

    # Обновляем пути в файле
    update_paths_in_config(file_path, train_path, test_path)

    print("Пути успешно обновлены в файле.")

if __name__ == "__main__":
    main()
