Инструкция по сборке:

(Я использовал для разработки Visual Studio Code)
![alt text](https://raw.githubusercontent.com/zzzlichzzz/-/refs/heads/main/Launcher/img.bmp?raw=true)

1) Иметь Python 3.12.8
2) На файле launcher.py запустить сборку в терминале
                         pyinstaller --onefile --add-data "src;src" launcher.py

после устрановки файл launcher.exe будет в папке "dist"
