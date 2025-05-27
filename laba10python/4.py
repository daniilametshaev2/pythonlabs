import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x = np.linspace(0, 2*np.pi, 400)

freq1_init = 1.0
amp1_init = 1.0
freq2_init = 1.0
amp2_init = 1.0

# Вычисляем исходные волны
y1 = amp1_init * np.sin(freq1_init * x)
y2 = amp2_init * np.sin(freq2_init * x)
y_sum = y1 + y2

# Создаем фигуру и оси для графиков
fig, axs = plt.subplots(3, 1, figsize=(10, 8))
plt.subplots_adjust(bottom=0.35)

# Первый график - волна 1
line1, = axs[0].plot(x, y1)
axs[0].set_title('Волна 1')
axs[0].grid(True)

# Второй график - волна 2
line2, = axs[1].plot(x, y2, color='orange')
axs[1].set_title('Волна 2')
axs[1].grid(True)

# Третий график - сумма волн
line3, = axs[2].plot(x, y_sum, color='green')
axs[2].set_title('Сумма волн')
axs[2].grid(True)

# Создаем оси для слайдеров под графиками
axcolor = 'lightgoldenrodyellow'
ax_freq1 = plt.axes([0.15, 0.25, 0.3, 0.03], facecolor=axcolor)
ax_amp1 = plt.axes([0.15, 0.20, 0.3, 0.03], facecolor=axcolor)
ax_freq2 = plt.axes([0.55, 0.25, 0.3, 0.03], facecolor=axcolor)
ax_amp2 = plt.axes([0.55, 0.20, 0.3, 0.03], facecolor=axcolor)

# Создаем слайдеры
slider_freq1 = Slider(ax_freq1, 'Частота Волна 1', 0.5, 5.0, valinit=freq1_init)
slider_amp1 = Slider(ax_amp1, 'Амплитуда Волна 1', 0.5, 3.0, valinit=amp1_init)
slider_freq2 = Slider(ax_freq2, 'Частота Волна 2', 0.5, 5.0, valinit=freq2_init)
slider_amp2 = Slider(ax_amp2, 'Амплитуда Волна 2', 0.5, 3.0, valinit=amp2_init)

def update(val):
    freq1 = slider_freq1.val
    amp1 = slider_amp1.val
    freq2 = slider_freq2.val
    amp2 = slider_amp2.val
    
    y1_new = amp1 * np.sin(freq1 * x)
    y2_new = amp2 * np.sin(freq2 * x)
    y_sum_new = y1_new + y2_new
    
    line1.set_ydata(y1_new)
    line2.set_ydata(y2_new)
    line3.set_ydata(y_sum_new)
    
    fig.canvas.draw_idle()

slider_freq1.on_changed(update)
slider_amp1.on_changed(update)
slider_freq2.on_changed(update)
slider_amp2.on_changed(update)

plt.show()
