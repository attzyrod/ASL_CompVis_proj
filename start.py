import cv2 #opencv
import os # help with file paths
import time #gonna use to take break in between images taken so we can move our hands
import uuid #to name image files

labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15
# change into directory that we'll be storing our images
os.chdir('Tensorflow/workspace/images/collectedImages/')
# Loop through label
for label in labels:
    # change into the folder holding images for this particular sign
    os.chdir(label)
    # start video capture (play around with because sometimes it might be 2 or 1)
    cap = cv2.VideoCapture(0)
    # To let us know what images are being collected for what sign
    print("Collecting images for {}".format(label))
    # Gives us time to get into position for image collection
    time.sleep(5)
    # Loop through images we want to collect (15)
    for imgnum in range(number_imgs):
        # Set up our capture (frame -> actual image)
        ret, frame = cap.read()
        # Defining captured image name with a specific image ID to prevent duplicates
        # and then writes file to current directory
        cv2.imwrite("./"+label+'_'+'{}.jpg'.format(str(uuid.uuid1())),frame)
        # Show the image collected
        cv2.imshow('frame', frame)
        # Give us time to get into other pose
        time.sleep(2)

        #If there's any issues we break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # go back to original folder
    os.chdir("..")
    # Release video capture
    cap.release()
