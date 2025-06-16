import os
import sys
import src.interface

def resource_path(relative_path):
    """ Получает абсолютный путь к ресурсу, работает для dev и для PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    # Получаем абсолютный путь к директории, в которой находится launcher.py
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Изменяем текущую рабочую директорию на директорию скрипта
    os.chdir(script_dir)

    # Запускаем интерфейс
    src.interface.create_interface()

if __name__ == "__main__":
    main()