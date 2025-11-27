import cv2 as cv
import numpy as np


def create_square_image(size=400, square_size=100, angle=0):

    img = np.zeros((size, size), dtype=np.uint8)
    cx, cy = size // 2, size // 2
    half = square_size // 2

    # Создаем вершины квадрата относительно центра
    pts = np.array([
        [cx - half, cy - half],
        [cx + half, cy - half],
        [cx + half, cy + half],
        [cx - half, cy + half]
    ], dtype=np.float32)

    if angle != 0:
        # Поворот вокруг центра квадрата
        # Матрица поворота: поворачиваем на angle градусов вокруг центра (cx, cy)
        M = cv.getRotationMatrix2D((cx, cy), angle, 1.0)
        pts = cv.transform(np.array([pts]), M)[0]

    pts = pts.astype(np.int32)
    cv.fillPoly(img, [pts], 255)  # Заливаем квадрат белым цветом
    return img


def apply_log_polar(img, center=None):

    if center is None:
        center = (img.shape[1] // 2, img.shape[0] // 2)

    # M - масштабный коэффициент, определяет "растяжение" лог-полярного изображения
    log_polar = cv.logPolar(img, center, M=40, flags=cv.INTER_LINEAR + cv.WARP_FILL_OUTLIERS)
    return log_polar


# Создаем четыре типа квадратов для исследования
# Большой квадрат (200x200)
big_square = create_square_image(square_size=200)
# Малый квадрат (100x100) - проверка инвариантности к масштабу
small_square = create_square_image(square_size=100)
# Большой повернутый квадрат - проверка инвариантности к вращению
big_square_rot = create_square_image(square_size=200, angle=45)
# Малый повернутый квадрат - комбинация масштаба и вращения
small_square_rot = create_square_image(square_size=100, angle=45)

squares = {
    "big_square": big_square,
    "small_square": small_square,
    "big_square_rot": big_square_rot,
    "small_square_rot": small_square_rot
}

#Применяем лог-полярные преобразования с разными центрами
log_polar_results = {}

for name, img in squares.items():
    # a) Центр в вершине квадрата (верхний левый угол холста)
    # Демонстрирует сложные искажения при выборе "плохого" центра
    center = (0, 0)
    log_polar_results[name + "_corner"] = apply_log_polar(img, center=center)

    # b) Центр внутри фигуры (смещен от центра к границе)
    # Показывает, как смещение центра влияет на результат преобразования
    center_inside = (img.shape[1] // 2 + 50, img.shape[0] // 2)
    log_polar_results[name + "_inside"] = apply_log_polar(img, center=center_inside)

    # c) Центр вне фигуры (за пределами изображения)
    # Демонстрирует периодические искажения при внешнем центре
    center_outside = (img.shape[1] + 20, img.shape[0] // 2)
    log_polar_results[name + "_outside"] = apply_log_polar(img, center=center_outside)

for name, img in log_polar_results.items():
    cv.imshow(name, img)

cv.waitKey(0)
cv.destroyAllWindows()