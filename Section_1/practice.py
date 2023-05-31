import cv2 as cv 

def resizedImg(frame, scale=0.75):
    width = int(frame.shape[1] * scale) 
    height = int(frame.shape[0] * scale) 

    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow("Cat", img)

resized_img = resizedImg(img)
cv.imshow("Resized_CatImg", resized_img)

cv.waitKey(0)

capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    resized_video = resizedImg(frame)
    cv.imshow('resized Video', resized_video)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break 
capture.release()
cv.destroyAllWindows()