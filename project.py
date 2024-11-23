import cv2
import numpy as np
p1=cv2.imread('flower.jpg')
print(p1)
cv2.imshow("window",p1)
cv2.waitKey(0)
img_gray=cv2.cvtColor(p1,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", img_gray)
cv2.waitKey(0)
cv2.imshow("Modified Image", p1)
cv2.waitKey(0)
p1[:,:,1]=0
cv2.imshow("modified image2:",p1)
cv2.waitKey(0)
p1[:,:,2]=0
cv2.imshow("modified image3:",p1)
cv2.waitKey(0)
yellow = p1.copy()
yellow[:, :, 0] = 0  # Remove blue channel
yellow[:, :, 1] = 255  # Max green channel
yellow[:, :, 2] = 255  # Max red channel
cv2.imshow("Yellow Image", yellow)
cv2.waitKey(0)
navy_blue = p1.copy()
navy_blue[:, :, 1] = navy_blue[:, :, 1] // 2  # Reduce green channel
navy_blue[:, :, 2] = 0  # Remove red channel
cv2.imshow("Navy Blue Image", navy_blue)
cv2.waitKey(0)
white = np.ones_like(p1) * 255
cv2.imshow("White Image", white)
cv2.waitKey(0)
imgblue=p1[:,:,0]
imggreen=p1[:,:,1]
imgred=p1[:,:,2]
new_img=np.hstack((imgblue,imggreen,imgred))
cv2.imshow("different types of color:",new_img)
cv2.waitKey(0)
blur=cv2.GaussianBlur(img_gray,(5,5),0)
cv2.imshow("blur:",blur)
cv2.waitKey(0)
black = np.zeros_like(p1)
cv2.imshow("Black Image", black)
cv2.waitKey(0)
edge=cv2.Canny(blur,10,70)
cv2.imshow("edge:",edge)
cv2.waitKey(0)
img_resize=cv2.resize(p1,(444,555))
cv2.imshow("window:",img_resize)
cv2.waitKey(0)
img_flip=cv2.flip(p1,-1)
cv2.imshow("flip:",img_flip)
cv2.waitKey(0)
img_crop=p1[0:450,0:400]
cv2.imwrite("flower small.png",img_crop)
cv2.imshow("image crop",img_crop)
cv2.waitKey(0)
# Read the image
# rectangle
img=np.zeros((1200,1600,3))
cv2.rectangle(img,pt1=(100,188),pt2=(200,300),color=(255,0,8),thickness=-1)
# circle
cv2.circle(img,center=(114,198),radius=50,color=(0,0,255),thickness=-1)
cv2.line(img,pt1=(0,8),pt2=(500,523),thickness=2,color=(0,255,8))
cv2.putText(img,org=(488,400),fontScale=4,color=(0,255,255),thickness=2,lineType=cv2.LINE_AA,text="hello world",fontFace=cv2.FONT_ITALIC)
cv2.imshow("draw:",img)
cv2.waitKey(0)