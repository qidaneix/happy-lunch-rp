import cv2
 
print 'it run 1'
cap=cv2.VideoCapture(0)
i=0
while(1):
    print 'it run 2'
    ret ,frame = cap.read()
    k=cv2.waitKey(1)
    if k==27:
        print 'it run 3'
        break
    elif k==ord('s'):
        print 'it run 4'
        cv2.imwrite(str(i)+'.jpg',frame)
        i+=1
    cv2.imshow("capture", frame)
cap.release()
cv2.destroyAllWindows()