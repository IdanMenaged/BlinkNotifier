import cv2

def main():
    while cv2.waitKey(1) != 27:
        cv2.imshow('winname', Camera().get_frame())
    
class Camera:    
    def __init__(self, *args):
        super(Camera, self).__init__(*args)
        
    def get_frame(self, device_index=0):
        """records a single frame

        Args:
            device_index (int, optional): represents the device index of input camera. Defaults to 0 (the default camera).

        Raises:
            Exception: when the program cannot record (ret == False)

        Returns:
            numpy.array: representing the frame
        """
        cap = cv2.VideoCapture(device_index)
        if not cap.isOpened():  # makes sure the camera was opened
            raise Exception('Could not open camera. Try to change your default camera?')
            
        ret, frame = cap.read()  # ret == True if the camera is recording, frame == numpy.array representing the frame
        if ret:
            cap.release()
            return frame
        else:
            raise Exception('Could not record')
        
    def show_frame(self, frame, winname, waitkey=27):
        """displays a given frame

        Args:
            frame (numpy.array): returned by the Camera.get_frame(self) method
            winname (string): the name of the window
            waitkey (int, optional): an ascii value representing a key. the image is displayed until said key is pressed. Defaults to 27 (ESC).
        """
        while cv2.waitKey(1) != waitkey:
            cv2.imshow(winname, frame)
    
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