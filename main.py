import cv2

def main():
    Camera().take_video()

class Camera:    
    def __init__(self, *args):
        super(Camera, self).__init__(*args)
        
    def get_frame(self):
        cap = cv2.VideoCapture(0)  # VideoCapture takes 0 for the default camera
        if not cap.isOpened():  # makes sure the camera was opened
            raise Exception('Could not open camera. Try to change your default camera?')
        ret, frame = cap.read()
        return frame
    
    def take_video(self):
        cap = cv2.VideoCapture(0)  # VideoCapture takes 0 for the default camera
        if not cap.isOpened():  # makes sure the camera was opened
            raise Exception('Could not open camera. Try to change your default camera?')
        
        while True:
            ret, frame = cap.read()  # ret == True if the camera is recording, frame == numpy.array representing the frame
            if not ret:
                break  # exit the loop when not recording
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == 27:  # detects when the ESC key was pressed (27 is the ASCII value of ESC)
                break
            
        cap.release()
        cv2.destroyAllWindows()
        
if __name__ == '__main__':
    main()