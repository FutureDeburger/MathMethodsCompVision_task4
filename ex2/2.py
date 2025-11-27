import cv2 as cv
import numpy as np


# a

# Создаем черное изображение 400x400 пикселей
img = np.zeros((400, 400), dtype=np.uint8)
# Рисуем белый заполненный квадрат от (50,50) до (350,350)
cv.rectangle(img, (50, 50), (350, 350), 255, -1)

# Центр лог-полярного преобразования - левая верхняя вершина квадрата
center = (50, 50)

# M - масштабный коэффициент для лог-полярного преобразования
# Определяет "масштаб" отображения радиальной координаты
M = 60

# Применяем лог-полярное преобразование
# cv.WARP_FILL_OUTLIERS - заполняет пиксели вне области исходного изображения
logpolar_square = cv.logPolar(img, center, M, cv.INTER_LINEAR + cv.WARP_FILL_OUTLIERS)

# cv.imshow("Original square", img)
# cv.imshow("Log-polar of square (center at vertex)", logpolar_square)
# cv.waitKey(0)
# cv.destroyAllWindows()


# b

# Создаем новое черное изображение
img2 = np.zeros((400, 400), dtype=np.uint8)
circle_center = (200, 200)  # Центр окружности
radius = 120  # Радиус окружности

# Рисуем окружность белым цветом толщиной 2 пикселя
cv.circle(img2, circle_center, radius, 255, 2)

# Центр преобразования смещен на 100 пикселей вправо от центра окружности
# Это помещает центр близко к правой границе окружности
center_inside = (200 + 100, 200)

logpolar_inside = cv.logPolar(img2, center_inside, 60, cv.INTER_LINEAR + cv.WARP_FILL_OUTLIERS)

# cv.imshow("Circle (center inside near edge)", img2)
# cv.imshow("Log-polar (center inside)", logpolar_inside)
# cv.waitKey(0)
# cv.destroyAllWindows()



# c

img3 = np.zeros((400, 400), dtype=np.uint8)
# Рисуем ту же окружность
cv.circle(img3, circle_center, radius, 255, 2)

# Центр преобразования смещен еще дальше - теперь вне окружности
center_outside = (200 + 140, 200)  # 140 > 120 (радиус), значит вне окружности
logpolar_outside = cv.logPolar(img3, center_outside, 60, cv.INTER_LINEAR + cv.WARP_FILL_OUTLIERS)

cv.imshow("Circle (center outside near edge)", img3)
cv.imshow("Log-polar (center outside)", logpolar_outside)
cv.waitKey(0)
cv.destroyAllWindows()