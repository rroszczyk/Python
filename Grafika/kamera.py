import cv2

vid = cv2.VideoCapture(0)

while (True):
    ret, frame = vid.read()
    
    frame = !frame      # negatyw
    #frame[:,:,0] = 0    # usunięcie jednego koloru
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
