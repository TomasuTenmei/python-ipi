import cv2

def resize(img, scale_percent:float) -> None:
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dimension =  width, height

    resized = cv2.resize(img, dimension, interpolation = cv2.INTER_AREA)
    return resized

image = cv2.imread('./imgs/DiscordBook.png')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_invert = cv2.bitwise_not(image_gray)
image_smoothing = cv2.GaussianBlur(image_invert, (21, 21), sigmaX=0, sigmaY=0)
pencil_sketch = cv2.divide(image_gray, 255 - image_smoothing, scale=256)

cv2.imshow('image', resize(image, 20))
cv2.imshow('image_gray', resize(image_gray, 20))
cv2.imshow('image_invert', resize(image_invert, 20))
cv2.imshow('image_smoothing', resize(image_smoothing, 20))
cv2.imshow('pencil_sketch', resize(pencil_sketch, 20))

cv2.waitKey()

cv2.destroyAllWindows()