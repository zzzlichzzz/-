from tkinter import filedialog

def select_directory():
    # Открываем диалоговое окно для выбора директории
    directory = filedialog.askdirectory()
    if directory:
        print(f"Выбрана директория: {directory}")
        return directory
    else:
        print("Директория не выбрана.")
        return None