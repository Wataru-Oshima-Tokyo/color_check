import cv2
import numpy as np
image_hsv= None   # global ;(
# pixel= (20,60,80) # some stupid default
# mouse callback function
def pick_color(event,x,y,flags,param):
    if event== cv2.EVENT_LBUTTONDOWN:
        pixel= image_hsv[y,x]
        #you might want to adjust the ranges(+-10, etc):
        upper=  np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
        lower=  np.array([pixel[0] -10, pixel[1] -10, pixel[2] -40])
        print(pixel, lower, upper)
        image_mask= cv2.inRange(image_hsv,lower,upper)
        # cv2.imshow("mask",image_mask)
        
def main():
    frameWidth = 640
    frameHeight = 480
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
    cap.set(10,150)
    while cap.isOpened():
        success, image_src = cap.read()
        if success:
            import sys
            global image_hsv, pixel # so we can use it in mouse callback
            if image_src is None:
                print ("the image read is None............")
                return
            cv2.imshow("bgr",image_src)
            ## NEW ##
            cv2.namedWindow('hsv')
            cv2.setMouseCallback('hsv', pick_color)
            # now click into the hsv img , and look at values:
            image_hsv= cv2.cvtColor(image_src,cv2.COLOR_BGR2HSV)
            cv2.imshow("hsv",image_hsv)
            cv2.imshow("Result", image_src)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__=='__main__':
    main()
