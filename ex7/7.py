import cv2 as cv
import numpy as np

# Загружаем изображения
image_files = ["img1.jpg", "img2.jpg", "img3.jpg"]  # замените на свои пути
images = [cv.imread(f) for f in image_files]

# Выравнивание гистограммы для каждого изображения
equalized_images = []
for img in images:
    if img is None:
        continue
    # если цветное изображение, переводим в YCrCb для работы с яркостью
    if len(img.shape) == 3:
        ycrcb = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
        ycrcb[:,:,0] = cv.equalizeHist(ycrcb[:,:,0])
        eq_img = cv.cvtColor(ycrcb, cv.COLOR_YCrCb2BGR)
    else:
        # если серое
        eq_img = cv.equalizeHist(img)
    equalized_images.append(eq_img)


for i, eq_img in enumerate(equalized_images):
    cv.imshow(f"Original {i}", images[i])
    cv.imshow(f"Equalized {i}", eq_img)

cv.waitKey(0)
cv.destroyAllWindows()