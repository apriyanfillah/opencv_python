import numpy as np
import cv2

biru = 255, 0, 0
jendela = np.zeros((500, 500, 3), dtype = 'uint8')
jendela[:] = (255, 0, 0)

cv2.rectangle(jendela, (125, 125), (375, 375),
              (255, 255, 255), 5)

cv2.imshow("Ini Kotak", jendela)
cv2.waitKey(0)