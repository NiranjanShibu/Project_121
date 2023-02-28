# import cv2 to capture videofeed
import cv2

import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# attach camera indexed as 0
camera = cv2.VideoCapture(0)

# setting framewidth and frameheight as 640 X 480
camera.set(3 , 640)
camera.set(4 , 480)

# loading the mountain image
mountain = cv2.imread('mount_everest.jpg')

while True:

    # read a frame from the attached camera
    status , frame = camera.read()

    # if we got the frame successfully
    if status:

        # flip it
        frame = cv2.flip(frame , 1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # converting the image to RGB for easy processing
        frame_rgb = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)

        # creating thresholds
        lower_bound = np.array([100, 100, 100])
        upper_bound = np.array([255, 255, 255])

        # thresholding image
        mask = cv2.inRange(hsv, lower_bound, upper_bound)
       

        # bitwise and operation to extract foreground / person
        res_1 = cv2.bitwise_and(frame, frame, mask)
        res_2 = cv2.bitwise_and(mountain, mountain, mask)
        
        #Generating the final output
        final_output = cv2.addWeighted(res_1, 1, res_2, 1, 0)
        output_file.write(final_output)
        
        #Displaying the output to the user
        cv2.imshow("magic", final_output)
        cv2.waitKey(1)

        # wait of 1ms before displaying another frame
        code = cv2.waitKey(1)
        if code  ==  32:
            break

# release the camera and close all opened windows
camera.release()
cv2.destroyAllWindows()
