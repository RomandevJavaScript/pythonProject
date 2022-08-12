import cv2
print("imported package")
cap = cv2.VideoCapture("image/MOV01814.AVI")
cap.set(3,640)
cap.set(4,480)
cap.set(10, 100)#настройка яркости изображения
# При нажатии на клавишу q видео закрывается
while True:
    success, img = cap.read()
    cv2.imshow("vid", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
# img = cv2.imread("image/DSC09729.JPG")
# cv2.imshow("Cote", img)
# cv2.waitKey(2000)