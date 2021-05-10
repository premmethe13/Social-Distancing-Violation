import cv2
import imagedetection
import time
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    
    img_name = "frame.jpg"
    cv2.imwrite(img_name, frame)
    
    imagedetection.new(img_counter)
    img_counter += 1
    print(img_counter)
    print("{} written!".format(img_name))
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    
        

cam.release()

cv2.destroyAllWindows()