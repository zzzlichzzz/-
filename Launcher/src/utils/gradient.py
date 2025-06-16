def create_gradient(canvas, width, height):
    # Цвета для градиента (в формате RGB)
    #color1 = (255, 230, 240)  # Очень светлый розовый
    #color2 = (230, 100, 150)  # Насыщенный розовый

    color1 = (170, 200, 220)  # Светло-морской
    color2 = (10, 30, 50)     # Глубокий океан
    # Создаем градиент на холсте
    for i in range(height):
        # Вычисляем промежуточный цвет
        ratio = i / height
        r = int(color1[0] + (color2[0] - color1[0]) * ratio)
        g = int(color1[1] + (color2[1] - color1[1]) * ratio)
        b = int(color1[2] + (color2[2] - color1[2]) * ratio)
        color = f'#{r:02x}{g:02x}{b:02x}'
        
        # Рисуем линию с вычисленным цветом
        canvas.create_line(0, i, width, i, fill=color)