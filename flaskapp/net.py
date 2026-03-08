from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os


# функция шахматного закрашивания
def chess_effect(image_path, percent):

    img = Image.open(image_path).convert("RGB")
    width, height = img.size

    # размер клетки в пикселях
    cell = int(width * percent / 100)

    pixels = np.array(img)

    for y in range(0, height, cell):
        for x in range(0, width, cell):

            if ((x // cell) + (y // cell)) % 2 == 0:

                pixels[y:y+cell, x:x+cell] = [0, 0, 0]

    new_img = Image.fromarray(pixels)

    result_path = "static/uploads/result.png"
    new_img.save(result_path)

    return result_path


# построение гистограммы цветов
def create_histogram(image_path, name):

    img = Image.open(image_path)

    histogram = img.histogram()

    plt.figure()
    plt.title(name)
    plt.plot(histogram)

    path = f"static/plots/{name}.png"
    plt.savefig(path)
    plt.close()

    return path