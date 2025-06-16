import tkinter as tk
import os
from tkinter import filedialog
from src.utils.gradient import create_gradient
from src.utils.functionL.build import build
from src.utils.functionL.selectDirectory import select_directory

# Глобальная переменная для хранения выбранной директории
selected_directory = None

# Файл для хранения выбранной директории
config_file = "config.txt"

def load_directory():
    global selected_directory
    if os.path.exists(config_file):
        with open(config_file, "r") as file:
            selected_directory = file.read().strip()

def save_directory(directory):
    with open(config_file, "w") as file:
        file.write(directory)

def set_selected_directory():
    global selected_directory
    selected_directory = select_directory()
    if selected_directory:
        save_directory(selected_directory)

def create_interface():
    root = tk.Tk()
    root.title("Сборка VoxelCore от Lich")

    # Загружаем сохраненную директорию
    load_directory()

    # Получаем размеры экрана
    screen_width = root.winfo_screenwidth() # Ширина экрана
    screen_height = root.winfo_screenheight() # Высота экрана

    # Устанавливаем размеры окна в процентном соотношении от размера экрана
    width = int(screen_height * 0.9)  # Ширина экрана
    height = int(screen_height * 0.6)  # Высоты экрана

    # Вычисляем координаты для центрирования окна
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Устанавливаем размеры окна и его позицию
    root.geometry(f"{width}x{height}+{x}+{y}")

    # Запрещаем изменять размер окна
    root.resizable(False, False)

    # Создаем холст
    canvas = tk.Canvas(root, width=width, height=height)
    canvas.pack(fill=tk.BOTH, expand=True)

    # Создаем градиент
    create_gradient(canvas, width, height)

    # Добавляем текст
    #canvas.create_text(width / 2, height / 2, text="Привет, мир", font=("Arial", 24), fill="azure")

    # Добавляем кнопку "Выбрать папку"

    select_button = tk.Button(root, text="Выбрать папку", command = set_selected_directory)
    select_button.place(relx=0.15, rely=0.85, anchor="center", relwidth=0.2, relheight=0.1)

    # Добавляем кнопку "Запуск сборки"
    
    button = tk.Button(root, text="Запуск сборки", command=lambda: build(selected_directory))
    button.place(relx=0.85, rely=0.85, anchor="center", relwidth=0.2, relheight=0.1)

    root.mainloop()