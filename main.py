import cv2

def main():
    while cv2.waitKey(1) != 27:
        cv2.imshow('winname', Camera().get_frame())

class Camera:    
    def __init__(self, *args):
        super(Camera, self).__init__(*args)
        
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():  # makes sure the camera was opened
            raise Exception('Could not open camera. Try to change your default camera?')
        
    def get_frame(self, device_index=0):
        """records a single frame
        put inside a `while cv2.waitKey(1) != 27` to record until the ESC key is pressed
        change 27 to any ascii value to change the key press needed

        Args:
            device_index (int, optional): represents the device index of input camera. Defaults to 0 (the default camera).

        Raises:
            Exception: when the program cannot record (ret == False)

        Returns:
            numpy.array: representing the frame
        """
        cap = cv2.VideoCapture(device_index)
            
        ret, frame = cap.read()  # ret == True if the camera is recording, frame == numpy.array representing the frame
        if ret:
            return frame
        else:
            raise Exception('Could not record')
    
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