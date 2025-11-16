import cv2 as cv
import numpy as np

# ------------------------------------------------------------
# (a) Лог-полярное преобразование квадрата, центр в вершине
# ------------------------------------------------------------

img = np.zeros((400, 400), dtype=np.uint8)
cv.rectangle(img, (50, 50), (350, 350), 255, -1)

center = (50, 50)

M = 60

logpolar_square = cv.logPolar(img, center, M, cv.INTER_LINEAR + cv.WARP_FILL_OUTLIERS)

cv.imshow("Original square", img)
cv.imshow("Log-polar of square (center at vertex)", logpolar_square)
cv.waitKey(0)
cv.destroyAllWindows()


# ------------------------------------------------------------
# (b) Окружность, центр лог-полярного преобразования внутри,
#     близко к границе окружности
# ------------------------------------------------------------

img2 = np.zeros((400, 400), dtype=np.uint8)
circle_center = (200, 200)
radius = 120

cv.circle(img2, circle_center, radius, 255, 2)

center_inside = (200 + 100, 200)

logpolar_inside = cv.logPolar(img2, center_inside, 60, cv.INTER_LINEAR + cv.WARP_FILL_OUTLIERS)

cv.imshow("Circle (center inside near edge)", img2)
cv.imshow("Log-polar (center inside)", logpolar_inside)
cv.waitKey(0)
cv.destroyAllWindows()


# ------------------------------------------------------------
# (c) Центр лог-полярного преобразования снаружи окружности,
#     близко к границе
# ------------------------------------------------------------

img3 = np.zeros((400, 400), dtype=np.uint8)
cv.circle(img3, circle_center, radius, 255, 2)

center_outside = (200 + 140, 200)

logpolar_outside = cv.logPolar(img3, center_outside, 60, cv.INTER_LINEAR + cv.WARP_FILL_OUTLIERS)

cv.imshow("Circle (center outside near edge)", img3)
cv.imshow("Log-polar (center outside)", logpolar_outside)
cv.waitKey(0)
cv.destroyAllWindows()