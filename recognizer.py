import cv2

def main():
    from camera import Camera
    img = Camera().get_frame()
    eyes = Recognizer().detect_eyes(img)
    Recognizer().draw_rectangle(eyes, img, winname='eyes')

class Recognizer:    
    def __init__(self, *args):
        super(Recognizer, self).__init__(*args)
        
    # TO DO: try to generelize it so that it can detect objects in general, not just eyes
    def detect_eyes(self, img):
        """detects all eyes in a given image

        Args:
            img (numpy.array): the image you wish to process

        Returns:
            tuple: representing a rectangle around the found eyes. the tuple consists of (x, y, w, h) where x and y are the top left coordinates while w and h are the width and the height of the rectangle
        """
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
        
        eyes = eye_cascade.detectMultiScale(img, 1.2, 5)
        return eyes
    
    # TO DO: seperate adding the rectangle and displaying the image
    def draw_rectangle(self, obj, img, color=(0, 255, 0), thickness=2, winname='image'):
        """adds a rectangle around an object in a given img

        Args:
            obj (tuple or list of tuples): consists of (x, y, w, h) representing x y coordinates, width, and height. can be multiple tuples
            img (numpy.array): the image you wish to add rectangles to
            color (tuple, optional): RGB value representing the color of the rectangole. Defaults to (0, 255, 0) which is green.
            thickness (int, optional): controls how thick the outline is. Defaults to 2.
            winname (str, optional): controls the name of the window in which the image is drawn. Defaults to 'image'.
        """
        for (x,y,w,h) in obj:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),color,thickness)
            
        cv2.imshow(winname, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
if __name__ == '__main__':
    main()