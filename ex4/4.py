import cv2 as cv
import numpy as np


def create_square_image(size=400, square_size=100, angle=0):
    """
    Создает изображение с квадратом.
    size: размер холста
    square_size: длина стороны квадрата
    angle: поворот квадрата в градусах
    """
    img = np.zeros((size, size), dtype=np.uint8)
    cx, cy = size // 2, size // 2
    half = square_size // 2
    pts = np.array([
        [cx - half, cy - half],
        [cx + half, cy - half],
        [cx + half, cy + half],
        [cx - half, cy + half]
    ], dtype=np.float32)

    if angle != 0:
        # поворот вокруг центра
        M = cv.getRotationMatrix2D((cx, cy), angle, 1.0)
        pts = cv.transform(np.array([pts]), M)[0]

    pts = pts.astype(np.int32)
    cv.fillPoly(img, [pts], 255)
    return img


def apply_log_polar(img, center=None):
    """
    Применяет лог-полярное преобразование
    center: центр лог-полярного преобразования
    """
    if center is None:
        center = (img.shape[1] // 2, img.shape[0] // 2)
    max_radius = np.sqrt((img.shape[1] / 2) ** 2 + (img.shape[0] / 2) ** 2)
    log_polar = cv.logPolar(img, center, M=40, flags=cv.INTER_LINEAR + cv.WARP_FILL_OUTLIERS)
    return log_polar


# --- создаём квадраты ---
big_square = create_square_image(square_size=200)
small_square = create_square_image(square_size=100)
big_square_rot = create_square_image(square_size=200, angle=45)
small_square_rot = create_square_image(square_size=100, angle=45)

squares = {
    "big_square": big_square,
    "small_square": small_square,
    "big_square_rot": big_square_rot,
    "small_square_rot": small_square_rot
}

# --- лог-полярные преобразования ---
log_polar_results = {}
for name, img in squares.items():
    # a) центр в вершине квадрата (верхний левый угол)
    center = (0, 0)
    log_polar_results[name + "_corner"] = apply_log_polar(img, center=center)
    # b) центр внутри фигуры (чуть ближе к границе)
    center_inside = (img.shape[1] // 2 + 50, img.shape[0] // 2)
    log_polar_results[name + "_inside"] = apply_log_polar(img, center=center_inside)
    # c) центр вне фигуры (чуть за границей)
    center_outside = (img.shape[1] + 20, img.shape[0] // 2)
    log_polar_results[name + "_outside"] = apply_log_polar(img, center=center_outside)


for name, img in log_polar_results.items():
    cv.imshow(name, img)

cv.waitKey(0)
cv.destroyAllWindows()