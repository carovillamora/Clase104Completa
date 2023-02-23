import cv2

# Leer la imagen
img = cv2.imread("butterfly.jpg")

# Muestra la imagen a color
cv2.imshow("Muestra la imagen",img)

# Convierte la imagen a color a una en escala de grises
gray_img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

# Muestra la imagen en escala de grises
cv2.imshow("Escala de grises", gray_img)

print(gray_img)

cv2.waitKey(0)
