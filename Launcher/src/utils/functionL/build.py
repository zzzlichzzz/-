import os
import shutil
import subprocess
import threading
import src.interface


def build(directory):
    def long_running_task():
        if directory:
            print("Сборка запущена")
            # Устанавливаем рабочую директорию
            os.chdir(directory)
            print(f"Текущая директория: {os.getcwd()}")

            # Проверяем, существует ли папка vcpkg
            if not os.path.exists("vcpkg"):
                # Если папки нет, клонируем репозиторий
                subprocess.run(["git", "clone", "https://github.com/microsoft/vcpkg.git"])
                print("vcpkg успешно скачан.")
            else:
                print("vcpkg уже существует.")

            # Переходим в папку vcpkg
            os.chdir("vcpkg")

            # Запускаем bootstrap-vcpkg.bat
            subprocess.run(["bootstrap-vcpkg.bat"])

            # Устанавливаем переменные окружения
            os.environ["VCPKG_ROOT"] = os.path.join(directory, "vcpkg")
            os.environ["PATH"] = os.path.join(os.environ["VCPKG_ROOT"], os.environ["PATH"])

            # Переходим в директорию VoxelCore
            os.chdir(directory)

            # Проверяем, существует ли папка VoxelEngine-Cpp
            if not os.path.exists("VoxelEngine-Cpp"):
                # Если папки нет, клонируем репозиторий
                subprocess.run(["git", "clone", "--recursive", "https://github.com/MihailRis/VoxelEngine-Cpp.git"])
                print("VoxelEngine-Cpp успешно скачан.")
            else:
                print("VoxelEngine-Cpp уже существует.")

            # Переходим в папку VoxelEngine-Cpp
            os.chdir("VoxelEngine-Cpp")

            # Пути к файлам мира и контента
            world_path = os.path.join(directory, "VoxelEngine-Cpp", "build", "Debug", "worlds")
            content_path = os.path.join(directory, "VoxelEngine-Cpp", "build", "Debug", "content")

            # Куда временно переносим сохранения
            destination_world_path = directory
            destination_content_path = directory

            # Перемещаем папки, если они существуют
            def move_directory_if_exists(source, destination):
                if os.path.exists(source):
                    try:
                        shutil.move(source, destination)
                        print(f"Папка '{source}' успешно перемещена в '{destination}'.")
                    except Exception as e:
                        print(f"Ошибка при перемещении папки: {e}")
                else:
                    print(f"Исходная папка '{source}' не существует.")

            move_directory_if_exists(world_path, destination_world_path)
            move_directory_if_exists(content_path, destination_content_path)

            # Проверяем, существует ли папка build
            if os.path.exists("build"):
                # Удаляем папку build
                shutil.rmtree("build")
                print("Папка 'build' успешно удалена.")
            else:
                print("Папка 'build' не существует.")

            # Запускаем cmake
            subprocess.run(["cmake", "--preset", "default-vs-msvc-windows"])
            subprocess.run(["cmake", "--build", "--preset", "default-vs-msvc-windows"])

            # Путь к сохраненным данным
            worlds = os.path.join(directory, "worlds")
            content = os.path.join(directory, "content")

            # Куда переносим сохраненные данные
            destination_world_content = os.path.join(directory, "VoxelEngine-Cpp", "build", "Debug")

            # Перемещаем папки
            shutil.move(worlds, destination_world_content)
            shutil.move(content, destination_world_content)

            import time
            time.sleep(5)  # Имитация длительной операции
            print("Сборка завершена")
        else:
            print("Директория не указана")
            print("Выбери директорию")
            src.interface.set_selected_directory()


    # Запускаем длительную операцию в отдельном потоке
    threading.Thread(target=long_running_task).start()