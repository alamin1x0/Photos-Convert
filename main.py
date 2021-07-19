import cv2
from imageio.core.util import Image
image = cv2.imread("py.png")
greyimg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
convert = cv2.bitwise_not(greyimg)
blur = cv2.GaussianBlur(convert,(35,35),0)
convertblur = cv2.bitwise_not(blur)
sketch = cv2.divide(greyimg, convertblur,scale=230.0)
cv2.imwrite("output.png",sketch)
