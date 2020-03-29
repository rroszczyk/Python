import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread("data/1_insole_L.jpg", 0)
# img = cv2.imread("data/1_leg_L.jpg", 0)
img = cv2.imread("data/1_L.jpg", 0)
img = cv2.GaussianBlur(img, (21, 21), cv2.BORDER_DEFAULT)

edges = cv2.Canny(img, 30, 40)

struct = np.ones((5, 5), np.uint8)
edges = cv2.dilate(edges, struct, iterations=1)
struct = np.ones((3, 3), np.uint8)
edges = cv2.erode(edges, struct, iterations=1)

fix, ax = plt.subplots(1, 2)
ax[0].imshow(img, cmap="gray")
ax[1].imshow(edges, cmap="gray")
plt.show()
