Инструкция по сборке:

(Я использовал для разработки Visual Studio Code)
![alt text](https://raw.githubusercontent.com/zzzlichzzz/-/refs/heads/main/Launcher/img.bmp?raw=true)

1) Иметь компилятор Python 3.12.8
2) В файлах проекта установить в ком.строке tkinter (Комманда уставновки - pip install tkinter )
3) На файле launcher.py запустить сборку в ком.строке
                         pyinstaller --onefile --add-data "src;src" launcher.py

после устрановки файл launcher.exe будет в папке "dist"
