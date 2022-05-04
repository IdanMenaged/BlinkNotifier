import cv2

def main():
    cv2.imshow('frame', Camera().get_frame())
    Camera().take_video()

class Camera:    
    def __init__(self, *args):
        super(Camera, self).__init__(*args)
        
    def get_frame(self):
        """get a single frame

        Raises:
            Exception: when camera does not open

        Returns:
            numpy_array: representing the image, can use cv2.imshow(winname, mat) with met as the array to display the image
        """
        cap = cv2.VideoCapture(0)  # VideoCapture takes 0 for the default camera
        ret, frame = cap.read()
        
        if not cap.isOpened() or not ret:  # makes sure the camera was opened
            raise Exception('Could not open camera. Try to change your default camera?')
        
        return frame
    
    def take_video(self):
        """take video until ESC key is pressed

        Raises:
            Exception: camera does not open
        """
        cap = cv2.VideoCapture(0)  # VideoCapture takes 0 for the default camera
        if not cap.isOpened():  # makes sure the camera was opened
            raise Exception('Could not open camera. Try to change your default camera?')
        
        while True:
            ret, frame = cap.read()  # ret == True if the camera is recording, frame == numpy.array representing the frame
            if not ret:
                break  # exit the loop when not recording
            
            cv2.imshow('video', frame)
            
            if cv2.waitKey(1) == 27:  # detects when the ESC key was pressed (27 is the ASCII value of ESC)
                break
            
        cap.release()
        cv2.destroyAllWindows()
        
if __name__ == '__main__':
    main()